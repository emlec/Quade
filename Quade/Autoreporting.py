# -*- coding: utf-8 -*-

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~IMPORTS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#


# Third party imports
import pandas as pd
from jinja2 import FileSystemLoader, Environment

# Local lib import


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~MAIN~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

def csv_to_html(filepath):
    """
    Open a .csv file and return it in HTML format.
    :param filepath: Filepath to a .csv file to be read.
    :return: String of HTML to be published.
    """
    df = pd.read_csv(filepath, index_col=0, delimiter="\t")
    html = df.to_html()
    return html


# Configure Jinja and ready the loader
env = Environment(
    loader=FileSystemLoader(searchpath="Quade/template")
)

# Assemble the templates we'll use
base_template = env.get_template("report.html")

# Content to be published

title = "Quade Report"
short_description = "Statistics obtained after demultiplexing using Quade"
csv_name = "Name of the corresponding CSV file : Quade_report.csv"
table = csv_to_html("test/result/Quade_report.csv")


def main():
    """
    Entry point for the script.
    Render a template and write it to file.
    :return:
    """
    with open("report.html", "w") as f:
        f.write(base_template.render(
            title=title,
            short_description=short_description,
            csv_name=csv_name,
            table=table
        ))


if __name__ == "__main__":
    main()
