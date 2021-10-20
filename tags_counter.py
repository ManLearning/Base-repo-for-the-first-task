import pandas as pd


with open("direct_search_post_jsonb1.csv", encoding="utf-8") as csvfile:
    df = pd.read_csv(csvfile, sep=';')
    tags = df.tgs  # change tgs to column name if needed

    tags_dict = {}
    for line in tags:
        if pd.isna(line):  # skipping NaNs
            continue
        line_tags_array = line.lower().split(',')
        for line_from_array in map(str.strip, line_tags_array):
            if line_from_array in tags_dict:
                tags_dict[line_from_array] += 1
            else:
                tags_dict.update({f"{line_from_array}": 1})

    print(tags_dict)
