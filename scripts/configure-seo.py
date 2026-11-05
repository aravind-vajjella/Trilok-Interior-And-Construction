#!/usr/bin/env python3
"""Write static search metadata. Supply --site-url once the production domain is known."""
import argparse, json, re, html
from pathlib import Path
from urllib.parse import urlsplit
from xml.sax.saxutils import escape
ROOT = Path(__file__).resolve().parents[1]
PAGES = {
 'index.html': ('Interior Design & Construction in Hyderabad | Trilok', 'Plan your home with Trilok: 2BHK and 3BHK interiors, modular kitchens, wardrobes and residential construction across Telangana and Andhra Pradesh.', 'Home', 'living-grand'),
 'services.html': ('Home Construction & Interior Design Services | Trilok', 'Explore house plans, residential construction, modular kitchens, wardrobes and fluted TV wall designs from Trilok in Telangana and Andhra Pradesh.', 'Services', 'fluted-detail'),
 'portfolio.html': ('Interior Design Concepts for Indian Homes | Trilok', 'Explore original AI-generated living room, kitchen and home construction concepts. Find your design direction and discuss your project with Trilok.', 'Design Concepts', 'living-warm'),
 'materials.html': ('Interior Materials & Wardrobe Design Guide | Trilok', 'Compare HDHMR, plywood and MDF considerations, explore wardrobe finishes and plan material choices for your home with Trilok Interiors & Construction.', 'Materials Guide', 'materials'),
 'calculator.html': ('Plan Your Interiors & Request a Custom Estimate | Trilok', 'Choose your property layout, area, interior style and construction scope. Send a personalized project brief to Trilok on WhatsApp for a tailored estimate.', 'Plan Your Project', 'living-grand')
}
def main():
 parser=argparse.ArgumentParser();parser.add_argument('--site-url');args=parser.parse_args()
 config_path=ROOT/'seo-config.json';config=json.loads(config_path.read_text()) if config_path.exists() else {'site_url':None}
 base=args.site_url or config.get('site_url')
 if base:
  u=urlsplit(base)
  if u.scheme!='https' or not u.hostname or '.' not in u.hostname or u.hostname in ['127.0.0.1','localhost'] or u.username or u.password or u.query or u.fragment or u.path not in ['', '/']:
   parser.error('Use the verified public HTTPS origin, without a path, query, credentials or fragment.')
  base=base.rstrip('/');config['site_url']=base
 config_path.write_text(json.dumps(config,indent=2)+'\n')
 def absolute(path):return (base+'/' if base else '')+path
 org={'@type':'Organization','@id':absolute('#organization'),'name':'Trilok Interiors & Construction','telephone':'+91-83320-98477','logo':absolute('logo.jpg'),'sameAs':['https://www.instagram.com/trilok._interior/'],'areaServed':[{'@type':'AdministrativeArea','name':'Telangana'},{'@type':'AdministrativeArea','name':'Andhra Pradesh'}]}
 if base:org['url']=base+'/'
 site={'@type':'WebSite','@id':absolute('#website'),'name':'Trilok Interiors & Construction','inLanguage':'en-IN','publisher':{'@id':org['@id']}}
 if base:site['url']=base+'/'
 for file,(title,description,label,photo) in PAGES.items():
  path=ROOT/file;s=path.read_text()
  s=re.sub(r'\s*<!-- SEO:START -->.*?<!-- SEO:END -->','',s,flags=re.S)
  s=re.sub(r'<title>.*?</title>', '',s,flags=re.S)
  s=re.sub(r'<meta\b[^>]*\b(?:name|property)="(?:description|keywords|robots|og:[^"]+|twitter:[^"]+)"[^>]*>', '',s)
  s=re.sub(r'<link\b[^>]*rel="canonical"[^>]*>', '',s)
  url=(base+'/' if file=='index.html' else absolute(file)) if base else None
  img=absolute(f'assets/generated/{photo}-1536.webp')
  esc=lambda value:html.escape(value,quote=True)
  entries=[f'<title>{esc(title)}</title>',f'<meta name="description" content="{esc(description)}">','<meta name="robots" content="index, follow, max-image-preview:large">','<meta name="theme-color" content="#111310">','<meta property="og:type" content="website">','<meta property="og:locale" content="en_IN">','<meta property="og:site_name" content="Trilok Interiors &amp; Construction">',f'<meta property="og:title" content="{esc(title)}">',f'<meta property="og:description" content="{esc(description)}">',f'<meta property="og:image" content="{esc(img)}">','<meta property="og:image:width" content="1536">','<meta property="og:image:height" content="1024">','<meta property="og:image:alt" content="Original AI-generated Trilok home design concept">','<meta name="twitter:card" content="summary_large_image">',f'<meta name="twitter:title" content="{esc(title)}">',f'<meta name="twitter:description" content="{esc(description)}">',f'<meta name="twitter:image" content="{esc(img)}">','<meta name="twitter:image:alt" content="Original AI-generated Trilok home design concept">']
  if url:entries.extend([f'<link rel="canonical" href="{esc(url)}">',f'<meta property="og:url" content="{esc(url)}">'])
  page={'@type':'CollectionPage' if file=='portfolio.html' else 'WebPage','@id':(url or file)+'#webpage','name':title,'description':description,'inLanguage':'en-IN','isPartOf':{'@id':site['@id']},'about':{'@id':org['@id']},'primaryImageOfPage':{'@type':'ImageObject','contentUrl':img,'caption':'Original AI-generated design concept'}}
  if url:page['url']=url
  graph=[org,site,page]
  if base and file!='index.html':
   graph.append({'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':base+'/'},{'@type':'ListItem','position':2,'name':label,'item':url}]});page['breadcrumb']={'@id':url+'#breadcrumb'}
  if file=='services.html':
   for name,anchor in [('House Plans & Residential Construction','construction'),('Modular Kitchens & Wardrobes','kitchen-wardrobe'),('Fluted Panels & TV Units','wall-panels')]:
    service={'@type':'Service','name':name,'serviceType':name,'provider':{'@id':org['@id']},'areaServed':org['areaServed']}
    if base:service['url']=url+'#'+anchor
    graph.append(service)
  entries.append('<script type="application/ld+json">'+json.dumps({'@context':'https://schema.org','@graph':graph},ensure_ascii=False).replace('</','<\\/')+'</script>')
  s=s.replace('</head>','\n<!-- SEO:START -->\n'+'\n'.join(entries)+'\n<!-- SEO:END -->\n</head>')
  # Keep the config command repeatable.
  s=re.sub(r'(<meta content="#111310" name="theme-color"/>)','',s)
  path.write_text(s)
 robots='User-agent: *\nAllow: /\nDisallow: /scripts/\n'
 if base:
  robots+='\nSitemap: '+base+'/sitemap.xml\n'
  urls=[base+'/' if p=='index.html' else base+'/'+p for p in PAGES]
  (ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'+''.join('  <url><loc>'+escape(url)+'</loc></url>\n' for url in urls)+'</urlset>\n')
 (ROOT/'robots.txt').write_text(robots)
 print('SEO generated for 5 pages. '+('Canonical URLs and sitemap configured for '+base if base else 'Public domain pending: canonical URLs and sitemap intentionally withheld.'))
if __name__=='__main__':main()
