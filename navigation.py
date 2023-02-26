import pandas as pd
import plotly.graph_objs as go
import matplotlib as plot
import folium
import dash_bootstrap_components as dbc
logo="assets/1.png"
navbar = dbc.Navbar(
    children=[
        dbc.Row(
            [
                dbc.Col(html.Img(src="/assets/capstone_logo.jpeg", height='50px'), style={'padding': '20px'}),
                dbc.Col(
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Home", href="/")),
                            dbc.NavItem(dbc.NavLink("About ", href="/aboutus")),
                            dbc.NavItem(dbc.NavLink("Services", href="/services")),
                            dbc.NavItem(dbc.NavLink("Contact ", href="/contactus")),
                        ],
                        navbar=True,
                        className="ml-auto",
                        style={'padding': '10px','margin-left':'500px'}
                    ),
                    width=8,
                ),
            ],
            # align='center' # add this property to align items side by side
        ),
    ],
    color="dark",
    dark=True,
)
# navbar = dbc.NavbarSimple(
#      children=[
#          dbc.NavItem(html.Img(src=logo, height="80px")),
#          dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#          dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#          dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#          dbc.NavItem(dbc.NavLink("Page 1", href="#")),
#          dbc.DropdownMenu(
#              children=[
#                  dbc.DropdownMenuItem("SECTIONS", header=True),
#                  dbc.DropdownMenuItem("FIRST YEAR", href="#"),
#                  dbc.DropdownMenuItem("SECOND YEAR", href="#"),
#                  dbc.DropdownMenuItem("THIRD YEAR", href="#"),
#                  dbc.DropdownMenuItem("FINAL YEAR", href="#"),
#              ],
#              nav=True,
#              in_navbar=True,
#              label="More",
#          ),
#      ],
#                  brand="",
#               brand_href="#",
#             color="primary",
#             dark=True,
# )
#
#  navbar = dbc.Navbar(
#     children=[
#         dbc.Row(
#             [
#                 dbc.Col(html.Img(src="/assets/logo.png", height="30px")),
#                 dbc.Col(
#                     dbc.Nav(
#                         [
#                             dbc.NavItem(dbc.NavLink("Home", href="/")),
#                             dbc.NavItem(dbc.NavLink("About Us", href="/aboutus")),
#                             dbc.NavItem(dbc.NavLink("Services", href="/services")),
#                             dbc.NavItem(dbc.NavLink("Contact Us", href="/contactus")),
#                         ],
#                         navbar=True,
#                         className="ml-auto",
#                     ),
#                     width=8,
#                 ),
#                 dbc.Col(html.Button("Help", color="primary", className="ml-2")),
#             ],
#             align="center",
#         ),
#     ],
#     color="dark",
#     dark=True,
# )
# dbc.Navbar(
#    dbc.Container(
#        [
#            dbc.Row(
#                [
#                    dbc.Col(html.Img(src=logo, height="80px")),
#
#                ]
#            ),
#                 dbc.Row(
#                [
#                     dbc.Col(dbc.NavLink("HELP", href="#")),
#
#                ]
#            ),
#            dbc.Row(
#                [
#                     dbc.DropdownMenu(
#                               children=[
#                                      dbc.DropdownMenuItem("SECTIONS", header=True),
#                                      dbc.DropdownMenuItem("FIRST YEAR", href="#"),
#                                      dbc.DropdownMenuItem("SECOND YEAR", href="#"),
#                                      dbc.DropdownMenuItem("THIRD YEAR", href="#"),
#                                      dbc.DropdownMenuItem("FINAL YEAR", href="#"),
#                                  ],
#                                  nav=True,
#                                  in_navbar=True,
#                                  label="PAGES",
#                              ),
#
#
#                ],
#            )
#        ]
#    ),
#
#
#     color="primary",
#     dark=True,
# )
