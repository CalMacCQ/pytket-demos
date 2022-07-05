import matplotlib.pyplot as plt

plt.style.use(["science", "notebook", "grid"])


def tuple_to_string1(tup: tuple) -> str: 
    """
    Converts a Tuple to a string as follows (1,0,0) -> "(1,0,0)".
    """
    return str(tup)


def dictionary_sorter(given_dict: dict, rank=6) -> dict: 
    """
    Sorts the Backend counts dictionary by value, its possible to only output the  
    most common measurement results by specifying the integer rank parameter.
    """

    sorted_values = sorted(given_dict.values(), reverse=True)
    sorted_dict = {}

    for i in sorted_values[:rank]:
        for k in given_dict.keys():
            if given_dict[k] == i:
                sorted_dict[k] = given_dict[k]
                break
    return sorted_dict

def format_results(result, rank: int) -> tuple([list,list]): 
    """
    Sorts experimental results and returns a tuple of sorted basis states and sorted count
    values to be plotted by plot_results.
    """
    sorted_experimental_results = dictionary_sorter(result.get_counts(), rank)
    sorted_result_keys = sorted_experimental_results.keys()
    sorted_basis_states = list(map(tuple_to_string1, sorted_result_keys)) # apply the tuple_to_string1 function to each basis state.
    sorted_count_values = list(sorted_experimental_results.values())
    return tuple([sorted_basis_states, sorted_count_values])

def plot_results(result, rank: int, title: str, n_shots=1000, save_png=False, optimisation=False):
    """
    Produces a bar chart for some input results basis states vs counts.
    Also takes a rank parameter r to show only show the r most common measurement results.
    """
    sorted_basis_states, sorted_count_values = format_results(result, rank) # unpack tuple of our formatted results.
    color_list = ["green"] + (["orange"] * (len(sorted_count_values) - 1))
    n_green_counts = sorted_count_values[0]  # number of measurements in our "correct" state

    fig = plt.figure()
    ax = fig.add_axes([0, 0, 2, 2])
    ax.bar(
        sorted_basis_states,
        sorted_count_values,
        color=color_list,
    )
    ax.set_title(title)
    plt.ylim([0, (0.65 * n_shots)])
    plt.xlabel("Basis State")
    plt.ylabel("Number of Shots")

    if save_png == True:
        if not optimisation:
            plt.savefig("qpe_results.png")
        else:
            plt.savefig("qpe_results_opt.png")

    print("Green counts:", n_green_counts, "out of", n_shots, "shots.")
    plt.show()

def plot_results_comparison(result1, result2, rank, n_shots=1000, save_png=False):
    """
    """
    sorted_basis_states, sorted_count_values = format_results(result1, rank)
    sorted_basis_states_opt, sorted_count_values_opt = format_results(result2, rank)
    color_list = ["green"] + (["orange"] * (len(sorted_count_values) - 1))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(28,8))

    fig.suptitle('Comparison of Naive vs Optimised Experiment', fontsize=24)

    ax1.bar(sorted_basis_states, sorted_count_values, color=color_list)
    ax1.set_xlabel('Basis state')
    ax1.set_ylabel('Number of Shots')
    ax1.set_ylim([0, (0.65 * n_shots)])

    ax2.bar(sorted_basis_states_opt, sorted_count_values_opt, color=color_list)
    ax2.set_xlabel('Basis state')
    ax2.set_ylim([0, (0.65 * n_shots)])
    ax2.set_yticks([])

    plt.subplots_adjust(wspace=0.05)


    if save_png == True:
        plt.savefig("qpe_results_comparison")

    plt.show()