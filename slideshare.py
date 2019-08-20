from lxml import html as _parse
import urllib.request
import img2pdf
import os

class slideshare():

  def __init__(self,url):
    self._url = url

#Faz download dos slides
  def download(self):
    _site = urllib.request.urlopen(self._url)
    _arvore = _parse.fromstring(_site.read())
    _site.close()
    _slides = _arvore.xpath('//img[@class="slide_image"]')
    slide_cntr=1
    for _slide in _slides:
      _s = _slide.get("data-full")
      urllib.request.urlretrieve("%s" % _s, "s_%0.9d.jpg" % slide_cntr)
      slide_cntr+=1

#Transforma em PDF
  def genPDF(self):
    with open("output.pdf", "wb") as f:
      f.write(img2pdf.convert([i for i in sorted(os.listdir(os.getcwd())) if i.endswith(".jpg")]))
    

#Deletando os arquivos as imagens apos o uso
  def distribution():
    try:
      return os.system("del s_*.jpg")
    except:
      return os.system("rm s_*.jpg")

#Baixa e faz o join
  def baixa(self):
    self.download()
    self.genPDF()

if __name__ == "__main__":
  import sys
  if len(sys.argv) != 2:
    print("slideshare.py -- Slideshare Downloader  ")
    print("sintaxe: ./slideshare.py [url]")
    sys.exit(1)
  else:
    slideshare(sys.argv[1]).baixa()
    slideshare.distribution()
    
#Renomeia o arquivo
    content = sys.argv[1]
    content = content.split('/')
    content = content[4] + '.pdf'
    os.rename('output.pdf', content)
