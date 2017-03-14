#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
main.py

Project: openweather

author  : Andreas Grätz
created : 14.03.2017
main    : andreaszdw@googlemail.com
"""
from kivy.network.urlrequest import UrlRequest

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class AddLocationForm(BoxLayout):
    search_input = ObjectProperty()

    def search_location(self):
        search_url = 'http://api.openweathermap.org/data/2.5/weather?q=Hüllhorst&units=metric&lang=de&appid=8d5a8025ecbf0f126f7a5fb60b60aeb6'  # <1>
        #search_url = search_template.format(self.search_input.text)
        request = UrlRequest(search_url, self.found_location) # <2>

    def found_location(self, request, data):  # <3>
        print data #b['name']
        '''cities = ["{} ({})".format(d['name'], d['sys']['country']) 
            for d in data['list']]  # <4>
        print("\n".join(cities))'''


class WeatherApp(App):
    pass

if __name__ == '__main__':
    WeatherApp().run()

    '''def got_weather(req, results):
        print req
        print results

    def got_failure(req, result):
        print "failure"
        print result

    def got_error(req, result):
        print "error"
        print result

    def got_progress(req, result):
        print "progress"
    
    print "starting"
    
    req = UrlRequest('http://api.openweathermap.org/data/2.5/weather?q=H%C3%BCllhorst&appid=8d5a8025ecbf0f126f7a5fb60b60aeb6',
        got_weather, on_failure=got_failure, on_error=got_error, on_progress=got_progress)

    print req

    raw_input("Press Enter")'''
