# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest
import pandas as pd

class CsvbotSpider(scrapy.Spider):
    name = 'csvbot'
    allowed_domains = ['jurisprudencia.stf.jus.br']
    script = '''
                   function main(splash, args)
                       assert(splash:go(args.url))
                       assert(splash:wait(1))
                       splash:set_viewport_full()
                       return splash:html()
                    end
               '''

    def start_requests(self):
        df = pd.read_csv('adi_links.csv')
        list = df.link.to_list()
        start_urls = list
        for i in range(0, len(start_urls)):
            yield SplashRequest(
                url=start_urls[i],
                callback=self.parse, endpoint="execute", args={
                    'lua_source': self.script
                })

    def parse(self, response):

        def find_key(val, dict):
            for key, value in dict.items():
                if value == val:
                    return key

        out_dict = {}
        trig = {}
        values = ["Ementa", 'Decisão', 'Indexação', 'Legislação', 'Observação', 'Acórdãos no mesmo sentido', 'Doutrina']
        for num in range(2, 13):
            val = response.xpath(f".//div[@class = 'cp-content display-in-print ng-star-inserted']/div[{num}]/h4/text()").get()
            if val is not None:
                trig[f"{num}"] = val.strip()
        for el in values:
            k = find_key(el, trig)
            if k is not None:
                    out_dict[f"{el}"] = response.xpath(f".//div[@class = 'cp-content display-in-print ng-star-inserted']/div[{k}]/div/text()").get().strip()
        out_dict.update({
            'nome': response.xpath(".//div[@class = 'jud-text']/h4[1]/text()").get(),
            'data_julgamento': response.xpath(".//div[@class = 'jud-text']/div/h4[1]/text()").get(),
            'data_publicacao': response.xpath(".//div[@class = 'jud-text']/div/h4[2]/text()").get(),
            'partes': response.xpath("//div/div[3]/div[@class = 'text-pre-wrap']/text()").get(),
            'link': response
            })

        yield out_dict