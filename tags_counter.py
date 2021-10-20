import pandas as pd


with open("normalized_dataset.csv", encoding="utf-8") as csvfile:
    df = pd.read_csv(csvfile, sep=';')
    tags = df["Tags"]  # change tgs to column name if needed
    tags = tags\
        .apply(
            lambda x: "" if not isinstance(x, str) else x.lower())\
        .apply(
            lambda x: list(map(str.strip, x.split(","))))
    sorterd_tags_counts = tags.explode().value_counts().sort_values(ascending=False)
    sorterd_tags_counts.to_csv("./sorted_tags_counts.csv")

    # tags.expand().value_counts
    # tags_dict = {}
    # for line in tags:
    #     if pd.isna(line):  # skipping NaNs
    #         continue
    #     line_tags_array = line.lower().split(',')
    #     for line_from_array in map(str.strip, line_tags_array):
    #         if line_from_array in tags_dict:
    #             tags_dict[line_from_array] += 1
    #         else:
    #             tags_dict.update({f"{line_from_array}": 1})
    # print(tags_dict)
