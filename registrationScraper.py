import urllib2
from HTMLParser import HTMLParser
from htmlentitydefs import name2codepoint
from bs4 import BeautifulSoup
import re
#Parser class
class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print "Start tag:", tag
        for attr in attrs:
            print "     attr:", attr

    def handle_endtag(self, tag):
        print "End tag  :", tag

    def handle_data(self, data):
        print "Data     :", data

    def handle_comment(self, data):
        print "Comment  :", data

    #def handle_entityref(self, name):
        #c = unichr(name2codepoint[name])
        #print "Named ent:", c

    def handle_charref(self, name):
        if name.startswith('x'):
            c = unichr(int(name[1:], 16))
        else:
            c = unichr(int(name))
        print "Num ent  :", c

    def handle_decl(self, data):
        print "Decl     :", data


def Scraper():
    #spring of 2019
    response = urllib2.urlopen("https://classes.aws.stthomas.edu/index.htm?year=2019&term=20&schoolCode=ALL&levelCode=ALL&selectedSubjects=ACCT,ACSC,ACST,AERO,AMBA,ARAB,ARHS,ARTH,BCHM,BCOM,BETH,BIOL,BLAW,BUSN,CATH,CHDC,CHEM,CHIN,CIED,CISC,CJUS,CLAS,COAC,COJO,COMM,CPSY,CSIS,CSMA,CTED,DRSW,DSCI,DVDM,DVDT,DVHS,DVLS,DVMT,DVPH,DVPM,DVPT,DVSP,DVSS,DVST,ECMP,ECON,EDCE,EDLD,EDUA,EDUC,EGED,ENGL,ENGR,ENTR,ENVR,ESCI,ETLS,EXSC,FAST,FILM,FINC,FREN,GBEC,GENG,GEOG,GEOL,GERM,GIFT,GMUS,GRED,GREK,GRPE,GRSW,GSPA,HIST,HLTH,HONR,HRDO,IBUS,IDSC,IDSW,IDTH,INAC,INCH,INEC,INEG,INFC,INFR,INGR,INHR,INID,INIM,INJP,INLW,INMC,INMG,INMK,INOP,INPS,INRS,INSP,INST,INTR,IRGA,ITAL,JAPN,JOUR,JPST,LATN,LAWS,LEAD,LGST,LHDT,MATH,MBAC,MBEC,MBEN,MBEX,MBFC,MBFR,MBFS,MBGC,MBGM,MBHC,MBHR,MBIF,MBIM,MBIS,MBLW,MBMG,MBMK,MBNP,MBOP,MBQM,MBSK,MBSP,MBST,MBUN,MBVE,MFGS,MGMP,MGMT,MKTG,MMUS,MSQS,MSRA,MUSC,MUSN,MUSP,MUSR,MUSW,NSCI,ODOC,OPMT,PHED,PHIL,PHYS,PLLD,POLS,PSYC,PUBH,QMCS,READ,REAL,RECE,REDP,RUSS,SABC,SABD,SACS,SAED,SAIM,SAIN,SALS,SAMB,SASE,SASW,SEAM,SEIS,SMEE,SOCI,SOWK,SPAN,SPED,SPGT,SPUG,STAT,STEM,TEGR,THEO,THTR,WMST")
    html = response.read()
    #f = open('response.html', 'w') #OPEN FILE WHEN USING
    #f.write(html)
    #parser = MyHTMLParser()
    #parser.feed(html)
    soup = BeautifulSoup(html, 'html.parser')
    #soup = soup.prettify().encode('utf-8')
    courses = soup.find_all('div', class_="course")
    for item in courses:
        courseNumber = item.find('span', class_='courseOpen').get_text() #This is NOT ID number
        courseName = item.find('div', class_='columns small-6 medium-4 large-4').get_text()
        courseName = " ".join(courseName.split())#This removes excess spaces
        courseTime = item.find('div', class_='columns small-6 medium-3 large-2').get_text()
        courseTime = " ".join(courseTime.split())#This removes excess spaces
        courseInst = item.find('div', class_='columns small-3 medium-2 large-2').get_text()
        courseInst = " ".join(courseInst.split())#This removes excess spaces
        courseLoca = item.find('span', class_='locationHover').get_text()
        courseLoca = " ".join(courseLoca.split())#This removes excess spaces
        courseCapa = item.find('div', class_='columns small-2').get_text()
        courseCapa = " ".join(courseCapa.split())#This removes excess spaces
        courseRegi = item.find_all('div', class_='columns small-3')#.get_text()
        courseRegi = " ".join(courseRegi[1].get_text().split())#This removes excess spaces

        courseInfo = item.find('p', class_='courseInfo').get_text()
        courseInfo = " ".join(courseInfo.split())#This removes excess spaces
        courseFied = item.find_all('p', class_='courseInfoHighlight')#.get_text()
        courseNumb = " ".join(courseFied[0].get_text().split())#This removes excess spaces
        courseCred = " ".join(courseFied[4].get_text().split())#This removes excess spaces
       
        print courseNumber
        print courseName
        print courseTime
        print courseInst
        print courseLoca
        print courseCapa
        print courseRegi
        print courseCred
        print courseNumb
        print courseInfo
        #f.write("%s\n" % item)
        break
    #f.write(courses)

Scraper()
