import matplotlib.pyplot as plt

plt.style.use(["science", "notebook", "grid"])


def tuple_to_string(tup):
    x = str(tup)
    return x


def dictionary_sorter(given_dict, rank=6):
    """
    Sorts the Backend counts dictionary by value, its possible to only output the  
    most common measurement results by specifying the rank parameter.
    """

    sorted_values = sorted(given_dict.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values[:rank]:
        for k in given_dict.keys():
            if given_dict[k] == i:
                sorted_dict[k] = given_dict[k]
                break
    return sorted_dict


def plot_results(result, rank, title):
    sorted_experimental_results = dictionary_sorter(result.get_counts(), rank)
    sorted_result_keys = sorted_experimental_results.keys()
    sorted_basis_states = list(map(tuple_to_string, sorted_result_keys))
    sorted_count_values = list(sorted_experimental_results.values())
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 2, 2])
    ax.bar(
        sorted_basis_states,
        sorted_count_values,
        color=["orange"] * len(sorted_count_values),
    )
    ax.set_title(title)
    plt.show()
