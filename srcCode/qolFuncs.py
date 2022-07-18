# ------------------QoL functions------------------#

# modules to import
import numpy as np
import shapely.geometry
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from plotly.subplots import make_subplots
pd.options.mode.chained_assignment = None
#from dash import Input, Output, State, dcc, html, callback
#import dash_bootstrap_components as dbc

import srcCode.qolDescs as qd

# Mapbox settings
mapbox_token_public = "pk.eyJ1IjoiZXZhbi10bSIsImEiOiJjbDFlYTlncTMwM2J3M2RwbDdjaXc2bW02In0.cxB8jf_1CFeoeVUAuOsYuA"
mapbox_style = "mapbox://styles/evan-tm/cl1ik4lmv003z15ru0ip4isbz"

# VDH OD death data
vdh = pd.read_csv('data/VDH.csv')
vdh = vdh[vdh['Death Rate'] != '*']
vdh['Death Rate'] = vdh['Death Rate'].astype(float)
# CDC Opioid dispensing data
cdcDispense = pd.read_csv('data/CDC_Dispense.csv')
# National prescription and OD death data
nationalData = pd.read_csv('data/nationalData.csv')
# VA Open Data Portal Office-Based Treatment data
offices = gpd.read_file("data/officeData.geojson")
offices = offices[offices['state'] == "VA"]


def plotUSALineplots():

    global nationalData
    fig = make_subplots(rows=1, cols=2, subplot_titles=['National Opioid Dispensing Rate Per 100 Persons',
                                                        'National Opioid Overdose Deaths Per 100,000 Persons'])
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['Opioid Dispensing Rate Per 100 Persons'],
                mode='lines+markers', name='Dispensing Rate', line=dict(color='blue', width=4)),
        row=1, col=1
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['AnyOpioidRate'], 
                mode='lines+markers', name='Any Opioids', line=dict(color='red', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['HeroinRate'], 
                mode='lines+markers', name='Heroin', line=dict(color='black', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['NatSemiSynthRate'], 
                mode='lines+markers', name='Natural or Semisynthetic', 
                line=dict(color='green', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['MethadoneRate'], 
                mode='lines+markers', name='Methadone', line=dict(color='purple', width=4)),
        row=1, col=2
    )
    fig.add_trace(
        go.Scatter(x=nationalData.Year, y=nationalData['SyntheticRate'], 
                mode='lines+markers', name='Other Synthetic',
                line=dict(color='darkgray', width=4)),
        row=1, col=2
    )
    fig.update_layout(plot_bgcolor = "#e8eaab")
    return fig

## Returns a plot of the VA office-based treatment facilities for OUD
## in: data from Virginia Open Data Portal
## out: figure representing the data
def plotOfficeMap():

    # offices chloropleth
    fig = px.scatter_mapbox(offices, 
                            lat=offices.geometry.y,
                            lon=offices.geometry.x,
                            hover_name = "name",
                            hover_data={"output_location": True},
                            center={"lat": 37.926868, "lon": -78.024902},
                            zoom=6)
    fig.update_layout(mapbox_accesstoken=mapbox_token_public, 
                    mapbox_style='light',
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    autosize=True,
                    font={'size': 16, 'color': "rgb(0,0,0)"})
    fig.update_traces(hovertemplate="<br>".join([
                                    "%{hovertext}",
                                    "",
                                    "Address:",
                                    "%{customdata[0]}"]))
    #fig.update_traces(hovertemplate=None, hoverinfo = 'skip')
    fig.update_yaxes(scaleanchor="x", scaleratio=1)

    return fig

## Returns a plot of the death rates for all opioids in VA
## in: data from VDH, year to plot, drug class
## out: figure representing the data
def plotVDHBar(year, drug_class, codes = None):
    
    plotData = vdh.loc[(vdh['Year of Death'] == year) & 
                       (vdh['Drug Class'] == drug_class)]
    if codes:
        plotData = plotData[plotData['Locality'].isin(codes)]
    # vdh chloropleth
    fig = px.bar(plotData.sort_values("Death Rate", ascending=True), 
                 x='Death Rate', y='Locality Name', height = 800)
    fig.update_layout(xaxis={'side': 'top'}, 
                    xaxis_title="Death Rate per 100,000 Persons",
                    xaxis_range=[0,91],
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font={'size': 12, 'color': "rgb(0,0,0)"},
                    height=len(plotData)*15)
    fig.update_traces(marker_color='rgb(158,202,225)', 
                      marker_line_color='rgb(8,48,107)',)
    
    return fig

## Returns a plot of the prescription rates for all opioids in VA
## in: data from CDC, year to plot, drug class
## out: figure representing the data
def plotCDCBar(year, state, codes = None):
    
    plotData = cdcDispense.loc[(cdcDispense['Year'] == year) & 
                               (cdcDispense['State'] == state)]
    plotData['County'] = plotData['County'].str.replace(', ' + state,'')
    plotData['County'] = plotData['County'].str.replace(r' County', '')
    plotData['County'] = plotData['County'].str.lower()
    plotData['County'] = plotData['County'].str.title()
    if codes:
        plotData = plotData[plotData['County FIPS Code'].isin(codes)]
    plotData = plotData[plotData['Opioid Dispensing Rate per 100'] != '–']
    plotData['Opioid Dispensing Rate per 100'] = plotData['Opioid Dispensing Rate per 100'].astype(float)
    # CDC bar plot
    fig = px.bar(plotData.sort_values("Opioid Dispensing Rate per 100", ascending=True), 
                 x='Opioid Dispensing Rate per 100', y='County')
    fig.update_layout(xaxis={'side': 'top'}, 
                    xaxis_title="Opioid Prescription Rate per 100 Persons",
                    xaxis_range=[0,600],
                    margin=go.layout.Margin(l=0, r=0,  b=0, t=0),
                    plot_bgcolor="rgba(0,0,0,0)",
                    paper_bgcolor="rgba(0,0,0,0)",
                    font={'size': 12, 'color': "rgb(0,0,0)"},
                    height=len(plotData)*15)
    fig.update_traces(marker_color='rgb(158,202,225)', 
                      marker_line_color='rgb(8,48,107)',)
    
    return fig