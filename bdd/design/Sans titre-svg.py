#!/usr/bin/env python
# encoding: utf-8
# Généré par Mocodo 1.6.1 le Sat, 20 Sep 2014 02:22:30

import time, codecs

try:
	import json
except ImportError:
	import simplejson as json

geo = json.loads(open("Sans titre-geo.json").read())
(width,height) = geo.pop("size")
for (name,l) in geo.iteritems(): globals()[name] = dict(l)
cardMaxWidth = 21
cardMaxHeight = 14
cardMargin = 5
arrowWidth = 12
arrowHalfHeight = 6
arrowAxis = 8

def cardPos(ex,ey,ew,eh,ax,ay,k):
	if ax!=ex and abs(float(ay-ey)/(ax-ex)) < float(eh)/ew:
		(x0,x1) = (ex+cmp(ax,ex)*(ew+cardMargin), ex+cmp(ax,ex)*(ew+cardMargin+cardMaxWidth))
		(y0,y1) = sorted([ey+(x0-ex)*(ay-ey)/(ax-ex), ey+(x1-ex)*(ay-ey)/(ax-ex)])
		return (min(x0,x1),(y0+y1-cardMaxHeight+k*abs(y1-y0+cardMaxHeight))/2+cmp(k,0)*cardMargin)
	else:
		(y0,y1) = (ey+cmp(ay,ey)*(eh+cardMargin), ey+cmp(ay,ey)*(eh+cardMargin+cardMaxHeight))
		(x0,x1) = sorted([ex+(y0-ey)*(ax-ex)/(ay-ey), ex+(y1-ey)*(ax-ex)/(ay-ey)])
		return ((x0+x1-cardMaxWidth+k*abs(x1-x0+cardMaxWidth))/2+cmp(k,0)*cardMargin,min(y0,y1))

def lineArrow(x0,y0,x1,y1,t):
	(x,y) = (t*x0+(1-t)*x1,t*y0+(1-t)*y1)
	return arrow(x,y,x1-x0,y0-y1)
	
def curveArrow(x0,y0,x1,y1,x2,y2,x3,y3,t):
	(cx,cy) = (3*(x1-x0),3*(y1-y0))
	(bx,by) = (3*(x2-x1)-cx,3*(y2-y1)-cy)
	(ax,ay) = (x3-x0-cx-bx,y3-y0-cy-by)
	t = 1-t
	bezier  = lambda t: (ax*t*t*t + bx*t*t + cx*t + x0, ay*t*t*t + by*t*t + cy*t + y0)
	(x,y) = bezier(t)
	u = 1.0
	while t < u:
		m = (u+t)/2.0
		(xc,yc) = bezier(m)
		d = ((x-xc)**2+(y-yc)**2)**0.5
		if abs(d-arrowAxis) < 0.01:
			break
		if d > arrowAxis:
			u = m
		else:
			t = m
	return arrow(x,y,xc-x,y-yc)

def upperRoundRect(x,y,w,h,r):
	return " ".join([unicode(x) for x in ["M",x+w-r,y,"a",r,r,90,0,1,r,r,"V",y+h,"h",-w,"V",y+r,"a",r,r,90,0,1,r,-r]])

def lowerRoundRect(x,y,w,h,r):
	return " ".join([unicode(x) for x in ["M",x+w,y,"v",h-r,"a",r,r,90,0,1,-r,r,"H",x+r,"a",r,r,90,0,1,-r,-r,"V",y,"H",w]])

def arrow(x,y,a,b):
	c = (a*a+b*b)**0.5
	(cos,sin) = (a/c,b/c)
	return " ".join([unicode(x) for x in [
		"M",x,y,
		"L",x+arrowWidth*cos-arrowHalfHeight*sin,y-arrowHalfHeight*cos-arrowWidth*sin,
		"L",x+arrowAxis*cos,y-arrowAxis*sin,
		"L",x+arrowWidth*cos+arrowHalfHeight*sin,y+arrowHalfHeight*cos-arrowWidth*sin,
		"Z"
	]])

def safePrint(s):
	try:
		print s
	except UnicodeEncodeError:
		print s.encode("utf8")


lines = '<?xml version="1.0" standalone="no"?>\n<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"\n"http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'
lines += '\n\n<svg width="%s" height="%s" viewBox="0 0 %s %s"\nxmlns="http://www.w3.org/2000/svg"\nxmlns:link="http://www.w3.org/1999/xlink">' % (width,height,width,height)
lines += u'\n\n<desc>Généré par Mocodo 1.6.1 le %s</desc>' % time.strftime("%a, %d %b %Y %H:%M:%S", time.localtime())
lines += '\n\n<rect x="0" y="0" width="%s" height="%s" fill="%s" stroke="none" stroke-width="0"/>' % (width,height,colors['backgroundColor'] if colors['backgroundColor'] else "none")

lines += u"""\n\n<!-- Association LOCALISATION -->"""
(x,y) = (cx[u"LOCALISATION"],cy[u"LOCALISATION"])
(ex,ey) = (cx[u"BIEN"],cy[u"BIEN"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,38,40,x,11.9+y,k[u"LOCALISATION,BIEN"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,1</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
(ex,ey) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,45,80,x,11.9+y,k[u"LOCALISATION,ADRESSE"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
lines += u"""\n<g id="association-LOCALISATION">""" % {}
path = upperRoundRect(-53+x,-24+y,106,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationCartoucheColor'], 'strokeColor': colors['associationCartoucheColor']}
path = lowerRoundRect(-53+x,0+y,106,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationColor'], 'strokeColor': colors['associationColor']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="106" height="48" fill="%(color)s" rx="14" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -53+x, 'y': -24+y, 'color': colors['transparentColor'], 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -53+x, 'y0': 0+y, 'x1': 53+x, 'y1': 0+y, 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">LOCALISATION</text>""" % {'x': -46+x, 'y': -7.1+y, 'textColor': colors['associationCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12"></text>""" % {'x': -46+x, 'y': 16.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association INTERVENTION -->"""
(x,y) = (cx[u"INTERVENTION"],cy[u"INTERVENTION"])
(ex,ey) = (cx[u"BIEN"],cy[u"BIEN"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,38,40,x,11.9+y,k[u"INTERVENTION,BIEN"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
(ex,ey) = (cx[u"PERSONNE"],cy[u"PERSONNE"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,42,40,x,11.9+y,k[u"INTERVENTION,PERSONNE"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
lines += u"""\n<g id="association-INTERVENTION">""" % {}
path = upperRoundRect(-60+x,-56+y,120,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationCartoucheColor'], 'strokeColor': colors['associationCartoucheColor']}
path = lowerRoundRect(-60+x,-32+y,120,88,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationColor'], 'strokeColor': colors['associationColor']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="120" height="112" fill="%(color)s" rx="14" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -60+x, 'y': -56+y, 'color': colors['transparentColor'], 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -60+x, 'y0': -32+y, 'x1': 60+x, 'y1': -32+y, 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">INTERVENTION</text>""" % {'x': -47+x, 'y': -39.1+y, 'textColor': colors['associationCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">motif</text>""" % {'x': -53+x, 'y': -15.1+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">date_echeance</text>""" % {'x': -53+x, 'y': 0.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">date_rdv</text>""" % {'x': -53+x, 'y': 16.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">etat_avancement</text>""" % {'x': -53+x, 'y': 32.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">commentaire</text>""" % {'x': -53+x, 'y': 48.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association LOCATION -->"""
(x,y) = (cx[u"LOCATION"],cy[u"LOCATION"])
(ex,ey) = (cx[u"BIEN"],cy[u"BIEN"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,38,40,x,11.9+y,k[u"LOCATION,BIEN"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
(ex,ey) = (cx[u"PERSONNE"],cy[u"PERSONNE"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,42,40,x,11.9+y,k[u"LOCATION,PERSONNE"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">0,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
lines += u"""\n<g id="association-LOCATION">""" % {}
path = upperRoundRect(-39+x,-24+y,78,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationCartoucheColor'], 'strokeColor': colors['associationCartoucheColor']}
path = lowerRoundRect(-39+x,0+y,78,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationColor'], 'strokeColor': colors['associationColor']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="78" height="48" fill="%(color)s" rx="14" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -39+x, 'y': -24+y, 'color': colors['transparentColor'], 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -39+x, 'y0': 0+y, 'x1': 39+x, 'y1': 0+y, 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">LOCATION</text>""" % {'x': -32+x, 'y': -7.1+y, 'textColor': colors['associationCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12"></text>""" % {'x': -32+x, 'y': 16.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Association PROPRIETE -->"""
(x,y) = (cx[u"PROPRIETE"],cy[u"PROPRIETE"])
(ex,ey) = (cx[u"BIEN"],cy[u"BIEN"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,38,40,x,11.9+y,k[u"PROPRIETE,BIEN"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
(ex,ey) = (cx[u"PERSONNE"],cy[u"PERSONNE"])
lines += u"""\n<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x0': ex, 'y0': ey, 'x1': x, 'y1': y, 'strokeColor': colors['legStrokeColor']}
(tx,ty) = cardPos(ex,11.9+ey,42,40,x,11.9+y,k[u"PROPRIETE,PERSONNE"])
lines += u"""\n<text x="%(tx)s" y="%(ty)s" fill="%(textColor)s" font-family="Verdana" font-size="12">1,N</text>""" % {'tx': tx, 'ty': ty, 'textColor': colors['cardTextColor']}
lines += u"""\n<g id="association-PROPRIETE">""" % {}
path = upperRoundRect(-41+x,-24+y,82,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationCartoucheColor'], 'strokeColor': colors['associationCartoucheColor']}
path = lowerRoundRect(-41+x,0+y,82,24,14)
lines += u"""\n	<path d="%(path)s" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'path': path, 'color': colors['associationColor'], 'strokeColor': colors['associationColor']}
lines += u"""\n	<rect x="%(x)s" y="%(y)s" width="82" height="48" fill="%(color)s" rx="14" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -41+x, 'y': -24+y, 'color': colors['transparentColor'], 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -41+x, 'y0': 0+y, 'x1': 41+x, 'y1': 0+y, 'strokeColor': colors['associationStrokeColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">PROPRIETE</text>""" % {'x': -34+x, 'y': -7.1+y, 'textColor': colors['associationCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12"></text>""" % {'x': -34+x, 'y': 16.9+y, 'textColor': colors['associationAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity PERSONNE -->"""
(x,y) = (cx[u"PERSONNE"],cy[u"PERSONNE"])
lines += u"""\n<g id="entity-PERSONNE">""" % {}
lines += u"""\n	<g id="frame-PERSONNE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="84" height="24" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -42+x, 'y': -40+y, 'color': colors['entityCartoucheColor'], 'strokeColor': colors['entityCartoucheColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="84" height="56" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -42+x, 'y': -16+y, 'color': colors['entityColor'], 'strokeColor': colors['entityColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="84" height="80" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -42+x, 'y': -40+y, 'color': colors['transparentColor'], 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -42+x, 'y0': -16+y, 'x1': 42+x, 'y1': -16+y, 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">PERSONNE</text>""" % {'x': -33+x, 'y': -23.1+y, 'textColor': colors['entityCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">personne_id</text>""" % {'x': -37+x, 'y': 0.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -37+x, 'y0': 3.0+y, 'x1': 37+x, 'y1': 3.0+y, 'strokeColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">nom</text>""" % {'x': -37+x, 'y': 16.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">prenom</text>""" % {'x': -37+x, 'y': 32.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity BIEN -->"""
(x,y) = (cx[u"BIEN"],cy[u"BIEN"])
lines += u"""\n<g id="entity-BIEN">""" % {}
lines += u"""\n	<g id="frame-BIEN">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="76" height="24" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -38+x, 'y': -40+y, 'color': colors['entityCartoucheColor'], 'strokeColor': colors['entityCartoucheColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="76" height="56" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -38+x, 'y': -16+y, 'color': colors['entityColor'], 'strokeColor': colors['entityColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="76" height="80" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -38+x, 'y': -40+y, 'color': colors['transparentColor'], 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -38+x, 'y0': -16+y, 'x1': 38+x, 'y1': -16+y, 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">BIEN</text>""" % {'x': -15+x, 'y': -23.1+y, 'textColor': colors['entityCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">bien_id</text>""" % {'x': -33+x, 'y': 0.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -33+x, 'y0': 3.0+y, 'x1': 11+x, 'y1': 3.0+y, 'strokeColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">type</text>""" % {'x': -33+x, 'y': 16.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">description</text>""" % {'x': -33+x, 'y': 32.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n</g>""" % {}

lines += u"""\n\n<!-- Entity ADRESSE -->"""
(x,y) = (cx[u"ADRESSE"],cy[u"ADRESSE"])
lines += u"""\n<g id="entity-ADRESSE">""" % {}
lines += u"""\n	<g id="frame-ADRESSE">""" % {}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="24" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -45+x, 'y': -80+y, 'color': colors['entityCartoucheColor'], 'strokeColor': colors['entityCartoucheColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="136" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="0"/>""" % {'x': -45+x, 'y': -56+y, 'color': colors['entityColor'], 'strokeColor': colors['entityColor']}
lines += u"""\n		<rect x="%(x)s" y="%(y)s" width="90" height="160" fill="%(color)s" stroke="%(strokeColor)s" stroke-width="2"/>""" % {'x': -45+x, 'y': -80+y, 'color': colors['transparentColor'], 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n		<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -45+x, 'y0': -56+y, 'x1': 45+x, 'y1': -56+y, 'strokeColor': colors['entityStrokeColor']}
lines += u"""\n	</g>""" % {}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">ADRESSE</text>""" % {'x': -29+x, 'y': -63.1+y, 'textColor': colors['entityCartoucheTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">adresse_id</text>""" % {'x': -40+x, 'y': -39.1+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<line x1="%(x0)s" y1="%(y0)s" x2="%(x1)s" y2="%(y1)s" stroke="%(strokeColor)s" stroke-width="1"/>""" % {'x0': -40+x, 'y0': -37.0+y, 'x1': 25+x, 'y1': -37.0+y, 'strokeColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">numero</text>""" % {'x': -40+x, 'y': -23.1+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">rue</text>""" % {'x': -40+x, 'y': -7.1+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">info</text>""" % {'x': -40+x, 'y': 8.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">ville</text>""" % {'x': -40+x, 'y': 24.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">code_postal</text>""" % {'x': -40+x, 'y': 40.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">commentaire</text>""" % {'x': -40+x, 'y': 56.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n	<text x="%(x)s" y="%(y)s" fill="%(textColor)s" font-family="Verdana" font-size="12">complement</text>""" % {'x': -40+x, 'y': 72.9+y, 'textColor': colors['entityAttributeTextColor']}
lines += u"""\n</g>""" % {}
lines += u'\n</svg>'

import codecs
codecs.open("Sans titre.svg","w","utf8").write(lines)
safePrint(u'Fichier de sortie "Sans titre.svg" généré avec succès.')