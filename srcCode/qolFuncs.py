# ------------------QoL functions------------------#

# modules to import
import numpy as np
import shapely.geometry
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import geopandas as gpd
from plotly.subplots import make_subplots      
import rioxarray                 # Surface data manipulation
import xarray                    # Surface data manipulation
from pysal.explore import esda   # Exploratory Spatial analytics
from pysal.lib import weights    # Spatial weights
import contextily                # Background tiles
from splot import esda as esdaplot
import plotly.figure_factory as ff
import matplotlib.pyplot as plt  # Graphics
from matplotlib import colors
import matplotlib
import base64
import os
pd.options.mode.chained_assignment = None
matplotlib.use('Agg')
#from dash import Input, Output, State, dcc, html, callback
#import dash_bootstrap_components as dbc

import srcCode.qolDescs as qd

# Mapbox settings
mapbox_token_public = "pk.eyJ1IjoiZXZhbi10bSIsImEiOiJjbDFlYTlncTMwM2J3M2RwbDdjaXc2bW02In0.cxB8jf_1CFeoeVUAuOsYuA"
mapbox_style = "mapbox://styles/evan-tm/cl1ik4lmv003z15ru0ip4isbz"

# VDH OD death data
vdh = pd.read_csv('data/VDH.csv')
vdhClean = vdh[vdh['Death Rate'] != '*']
vdhClean['Death Rate'] = vdhClean['Death Rate'].astype(np.float64)
# CDC Opioid dispensing data
cdcDispense = pd.read_csv('data/CDC_Dispense.csv')
# Extract VA data from CDC dispensing data
vaDispense = cdcDispense.loc[cdcDispense['State'] == 'VA']
vaDispense['County FIPS Code'] = vaDispense['County FIPS Code'].astype(int)
vaDispense['County'] = vaDispense['County'].str.replace(', VA','')
vaDispense['County'] = vaDispense['County'].str.replace(r' County', '')
vaDispense['County'] = vaDispense['County'].str.lower()
vaDispense['County'] = vaDispense['County'].str.title()
# VA Geography
geofile = "data/vaGeo.geojson"
vaGeo = gpd.read_file(geofile)
vaGeo['geoid'] = vaGeo['geoid'].astype(str).astype(int)
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
    
    plotData = vdhClean.loc[(vdhClean['Year of Death'] == year) & 
                       (vdhClean['Drug Class'] == drug_class)]
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

## Get LISA dataframes given the year, target variable, and drug class
## in: year to gather, target variable, drug class
## out: database with standardized weights, lisa object
def getLISAframes(year, target = 'od', drug_class='Any Opioids'):
    if target == 'od':
        # Filter df
        moranDF = vdh.loc[(vdh['Year of Death'] == year) & (vdh['Drug Class'] == drug_class)]
        # Replace suppressed data with 0's
        moranDF['Death Rate'].loc[moranDF['Death Rate'] == '*'] = 0.0
        moranDF['Death Rate'] = moranDF['Death Rate'].astype(np.float64)
        # Build merged db
        db = moranDF.merge(vaGeo, left_on='Locality', right_on = 'geoid', how='left')
        db = gpd.GeoDataFrame(db)
        # Filter
        db = db[['Year of Death', 'Locality', 'Drug Class', 'Death Count', 'Death Rate', 'geometry']]
        # Generate W from the GeoDataFrame
        w = weights.distance.KNN.from_dataframe(db, k=8)
        # Row-standardization
        w.transform = 'R'
        db['w_Death_Rate'] = weights.spatial_lag.lag_spatial(w, db['Death Rate'])
        db['Death_Rate_stdize'] = ( db['Death Rate'] - db['Death Rate'].mean() )
        db['w_Death_Rate_stdize'] = ( db['w_Death_Rate'] - db['Death Rate'].mean() )
        lisa = esda.moran.Moran_Local(db['Death Rate'], w)
    else:
        moranDF = vaDispense.loc[(vaDispense['Year'] == year)]
        moranDF = moranDF[moranDF['Opioid Dispensing Rate per 100'] != '–']
        moranDF['Opioid Dispensing Rate per 100'] = moranDF['Opioid Dispensing Rate per 100'].astype(np.float64)
        # Build merged db
        db = moranDF.merge(vaGeo, left_on='County FIPS Code', right_on = 'geoid', how='left')
        db = gpd.GeoDataFrame(db)
        # Filter
        db = db[['Year', 'County FIPS Code', 'Opioid Dispensing Rate per 100', 'geometry']]
        # Generate W from the GeoDataFrame
        w = weights.distance.KNN.from_dataframe(db, k=8)
        # Row-standardization
        w.transform = 'R'
        db['w_Rx'] = weights.spatial_lag.lag_spatial(w, db['Opioid Dispensing Rate per 100'])
        db['Rx_stdize'] = ( db['Opioid Dispensing Rate per 100'] - db['Opioid Dispensing Rate per 100'].mean() )
        db['w_Rx_stdize'] = ( db['w_Rx'] - db['Opioid Dispensing Rate per 100'].mean() )
        lisa = esda.moran.Moran_Local(db['Opioid Dispensing Rate per 100'], w)
    
    return db, lisa

def plotMoran(db, target = 'od'):
    if target == 'od':
        fig = px.scatter(db, x='Death_Rate_stdize', y='w_Death_Rate_stdize',
                 width=500, height=500, trendline="ols")
        fig.add_hline(y=0, opacity=0.5)
        fig.add_vline(x=0, opacity=0.5)
    else:
        fig = px.scatter(db, x='Rx_stdize', y='w_Rx_stdize',
                 width=500, height=500, trendline="ols")
        fig.add_hline(y=0, opacity=0.5)
        fig.add_vline(x=0, opacity=0.5)
    return fig

def plotKDE(lisa):
    return ff.create_distplot([lisa.Is], group_labels = ['Local Indicators'], show_hist=False)

def plotClusters(db, lisa):
    # Set up figure and axes
    f, axs = plt.subplots(nrows=2, ncols=2, figsize=(12, 12))
    # Make the axes accessible with single indexing
    axs = axs.flatten()

                        # Subplot 1 #
                # Choropleth of local statistics
    # Grab first axis in the figure
    ax = axs[0]
    # Assign new column with local statistics on-the-fly
    db.assign(
        Is=lisa.Is
    # Plot choropleth of local statistics
    ).plot(
        column='Is', 
        cmap='plasma', 
        scheme='quantiles',
        k=5, 
        edgecolor='white', 
        linewidth=0.1, 
        alpha=0.75,
        legend=True,
        ax=ax
    )

                        # Subplot 2 #
                    # Quadrant categories
    # Grab second axis of local statistics
    ax = axs[1]
    # Plot Quandrant colors (note to ensure all polygons are assigned a
    # quadrant, we "trick" the function by setting significance level to
    # 1 so all observations are treated as "significant" and thus assigned
    # a quadrant color
    esdaplot.lisa_cluster(lisa, db, p=1, ax=ax);

                        # Subplot 3 #
                    # Significance map
    # Grab third axis of local statistics
    ax = axs[2]
    # 
    # Find out significant observations
    labels = pd.Series(
        1 * (lisa.p_sim < 0.05), # Assign 1 if significant, 0 otherwise
        index=db.index           # Use the index in the original data
    # Recode 1 to "Significant and 0 to "Non-significant"
    ).map({1: 'Significant', 0: 'Non-Significant'})
    # Assign labels to `db` on the fly
    db.assign(
        cl=labels
    # Plot choropleth of (non-)significant areas
    ).plot(
        column='cl', 
        categorical=True,
        k=2,
        cmap='Paired',
        linewidth=0.1,
        edgecolor='white',
        legend=True,
        ax=ax
    )


                        # Subplot 4 #
                        # Cluster map
    # Grab second axis of local statistics
    ax = axs[3]
    # Plot Quandrant colors In this case, we use a 5% significance
    # level to select polygons as part of statistically significant
    # clusters
    esdaplot.lisa_cluster(lisa, db, p=0.05, ax=ax);

                        # Figure styling #
    # Set title to each subplot
    for i, ax in enumerate(axs.flatten()):
        ax.set_axis_off()
        ax.set_title(
            [
                'Local Statistics', 
                'Scatterplot Quadrant', 
                'Statistical Significance', 
                'Moran Cluster Map'
            ][i], y=-0.2
        )
    # Tight layout to minimise in-betwee white space
    f.tight_layout()
    plt.savefig('clusters.png', bbox_inches='tight')
    image_filename = os.path.join(os.getcwd(), 'clusters.png')
    encoded_image = base64.b64encode(open(image_filename, 'rb').read())
    return encoded_image