from pathlib import Path
import re, xml.etree.ElementTree as ET
from html.parser import HTMLParser
root=Path(__file__).resolve().parents[1]
class H(HTMLParser):
 def __init__(self):
  super().__init__();self.tags=[];self.ids=[];self.labels=[];self.fields=[]
 def handle_starttag(self,t,attrs):
  d=dict(attrs);self.tags.append(t)
  if 'id' in d:self.ids.append(d['id'])
  if t=='label':self.labels.append(d.get('for'))
  if t in ('input','textarea'):self.fields.append((d.get('id'),d.get('type')))
pages=list(root.rglob('index.html'))
assert len(pages)==7, len(pages)
for p in pages:
 raw=p.read_text(encoding='utf-8');h=H();h.feed(raw)
 assert h.tags.count('h1')==1,p
 assert '<link rel="canonical"' in raw,p
 assert '<meta name="description"' in raw or 'name="description"' in raw,p
 assert len(h.ids)==len(set(h.ids)),p
 for i,t in h.fields:
  if i and t!='hidden': assert i in h.labels,(p,i)
 assert not re.search(r'UGC CARE-listed|250\+ premium|300\+ journals',raw),p
s=ET.parse(root/'sitemap.xml').getroot()
urls=[n.text for n in s.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc')]
assert len(urls)==len(set(urls))
for p in pages:
 url='https://www.everestperiodicals.com/'+('' if p.parent==root else p.parent.relative_to(root).as_posix()+'/')
 assert url in urls,(p,url)
assert 'Sitemap:' in (root/'robots.txt').read_text()
home=(root/'index.html').read_text()
assert 'aria-live="polite"' in home and 'aria-expanded="false"' in home and 'faq-answer-3' in home
print('Source checks pass. Live HTTP and browser testing still required.')
