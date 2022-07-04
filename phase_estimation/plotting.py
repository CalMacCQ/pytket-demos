import matplotlib.pyplot as plt
from typing import Optional

plt.style.use(["science", "notebook", "grid"])


def tuple_to_string1(tup: tuple) -> str: 
    """
    Converts a Tuple to a string as follows (1,0,0) -> "(1,0,0)"
    """
    return str(tup)


def dictionary_sorter(given_dict: dict, rank=6) -> dict: 
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


def plot_results(result, rank: int, title:str, n_shots=1000, save_png=False, optimisation=False):
    """
    Produces a bar chart for some input results basis states vs counts.
    Also takes a rank parameter r to show only show the r most common measurement results.
    """

    sorted_experimental_results = dictionary_sorter(result.get_counts(), rank)
    sorted_result_keys = sorted_experimental_results.keys()
    sorted_basis_states = list(map(tuple_to_string1, sorted_result_keys))
    sorted_count_values = list(sorted_experimental_results.values())
    n_green_counts = sorted_count_values[0]  # number of measurements in our "correct" state

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 2, 2])
    ax.bar(
        sorted_basis_states,
        sorted_count_values,
        color=["green"] + (["orange"] * (len(sorted_count_values) - 1)),
    )
    ax.set_title(title)
    plt.ylim([0, (0.65 * n_shots)])
    plt.xlabel("Basis States")
    plt.ylabel("Number of Shots")

    if save_png == True:
        if not optimisation:
            plt.savefig("qpe_results.png")
        else:
            plt.savefig("qpe_results_opt.png")

    print("Green counts:", n_green_counts, "out of", n_shots, "shots.")
    plt.show()
