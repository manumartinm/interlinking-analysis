import streamlit as st
import pandas as pd
from utils import match_inlinks, colors_index, size_of_node
import networkx as nx
import numpy as np
from matplotlib import pyplot as plt

st.title("Analyse the Interlining of your web page")

domain = st.text_input("Enter the domain of your web page:", "")
interlinking_csv = st.file_uploader("Upload the interlinking csv of SF", type=["csv"])
internal_html_csv = st.file_uploader("Upload the internal html csv of SF", type=["csv"])

if interlinking_csv is not None and internal_html_csv is not None and domain != "":
    inlinks_df = pd.read_csv(interlinking_csv)
    interl_html_df = pd.read_csv(internal_html_csv)
    list_inlinks = inlinks_df.values.tolist()
    list_internal_html = interl_html_df.values.tolist()
    
    tuples_inlinks = match_inlinks(list_inlinks, domain)
    G = nx.Graph()
    G.add_edges_from(tuples_inlinks)

    colors_list = colors_index(G.nodes, list_internal_html)
    sorted_dictionary = size_of_node(G.degree)
    
    pos = nx.spring_layout(G, k=0.3*1/np.sqrt(len(G.nodes())), iterations=20)
    plt.figure(3, figsize=(30, 30))
    dictionary_degree = dict(G.degree)

    nx.draw(G, pos, with_labels=False, node_size=[10 + v * 300 for v in dictionary_degree.values()], node_color=colors_list, font_size=15)
    nx.draw_networkx_labels(G, pos, sorted_dictionary,font_size=25, font_color='r')

    plt.savefig("graph.png")

    plt.show()
