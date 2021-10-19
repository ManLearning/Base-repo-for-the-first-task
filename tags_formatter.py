import pandas as pd


def generate_marked_dataset(unmarked_dataset: pd.DataFrame, tags_to_include: list):
    interior_unmarked_dataset = unmarked_dataset
    marked_dataset: pd.DataFrame = interior_unmarked_dataset.drop(
        labels="Tags", axis="columns")
    for single_tag in map(str.lower, tags_to_include):
        marked_dataset[single_tag] = interior_unmarked_dataset["Tags"].apply(
            lambda x: 1 if single_tag in x else 0)
    return marked_dataset


if __name__ == "__main__":
    unmarked_dataset = pd.read_csv(
        "./direct_search_post_jsonb1.csv", sep=";")

    unmarked_dataset.rename(columns={
        "ttl": "Title",
        "txt": "FormattedText",
        "cln_txt": "PlainText",
        "tgs": "Tags"
    }, inplace=True)

    unmarked_dataset["Tags"] = unmarked_dataset["Tags"]\
        .apply(
            lambda x: "" if not isinstance(x, str) else x)\
        .apply(
            lambda x: x.lower().split(","))

    tags_to_include = ['растениеводство']

    filtered_dataset = generate_marked_dataset(unmarked_dataset,
                                               tags_to_include)

    print(filtered_dataset[filtered_dataset[tags_to_include[0]] == 1])
