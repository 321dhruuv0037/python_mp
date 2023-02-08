import dash_bootstrap_components.themes
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import plotly.graph_objs as go
import matplotlib as plot
import folium
import dash_bootstrap_components as dbc
logo="assets/1.png"


# navbar = dbc.NavbarSimple(
#     children=[
#         dbc.NavItem(html.Img(src=logo, height="80px")),
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#         dbc.DropdownMenu(
#             children=[
#                 dbc.DropdownMenuItem("SECTIONS", header=True),
#                 dbc.DropdownMenuItem("FIRST YEAR", href="#"),
#                 dbc.DropdownMenuItem("SECOND YEAR", href="#"),
#                 dbc.DropdownMenuItem("THIRD YEAR", href="#"),
#                 dbc.DropdownMenuItem("FINAL YEAR", href="#"),
#             ],
#             nav=True,
#             in_navbar=True,
#             label="More",
#         ),
#     ],
#     brand="",
#     brand_href="#",
#     color="primary",
#     dark=True,
# )

navbar = dbc.Navbar(
   dbc.Container(
       [
           dbc.Row(
               [
                   dbc.Col(html.Img(src=logo, height="80px")),

               ]
           ),
                dbc.Row(
               [
                    dbc.Col(dbc.NavLink("HELP", href="#")),

               ]
           ),
           dbc.Row(
               [
                    dbc.DropdownMenu(
                              children=[
                                     dbc.DropdownMenuItem("SECTIONS", header=True),
                                     dbc.DropdownMenuItem("FIRST YEAR", href="#"),
                                     dbc.DropdownMenuItem("SECOND YEAR", href="#"),
                                     dbc.DropdownMenuItem("THIRD YEAR", href="#"),
                                     dbc.DropdownMenuItem("FINAL YEAR", href="#"),
                                 ],
                                 nav=True,
                                 in_navbar=True,
                                 label="PAGES",
                             ),


               ],
           )
       ]
   ),


    color="primary",
    dark=True,
)
