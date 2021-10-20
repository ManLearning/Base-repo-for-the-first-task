import pandas as pd


def generate_marked_dataset(unmarked_dataset: pd.DataFrame, tags_to_include: list):
    marked_dataset: pd.DataFrame = unmarked_dataset.drop(
        labels="Tags", axis="columns")
    for single_tag in map(str.lower, tags_to_include):
        marked_dataset[single_tag] = unmarked_dataset["Tags"].apply(
            lambda x: 1 if single_tag in x else 0)
    return marked_dataset


def generate_and_export_marked_dataset(unmarked_dataset: pd.DataFrame, tags_to_include: list):
    filtered_dataset = generate_marked_dataset(unmarked_dataset,
                                               tags_to_include)
    filtered_dataset.to_csv(
        "./filtered_dataset_{}.csv".format("_".join(tags_to_include)), index=False, sep=";")


# This part is just for demonstration
if __name__ == "__main__":
    unmarked_dataset = pd.read_csv(
        "./normalized_dataset.csv", sep=";")

    unmarked_dataset["Tags"] = unmarked_dataset["Tags"].apply(
        lambda x: x.split(',') if isinstance(x, str) else [])

    tags_to_include = ['животноводство', 'растениеводство']

    generate_and_export_marked_dataset(unmarked_dataset,
                                       tags_to_include)
