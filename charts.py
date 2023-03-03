import matplotlib.pyplot as plt


def generate_bar_chart(labels, values):
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()


if __name__ == '__main__':
    labels = ['a', 'b', 'c']
    values = [100, 80, 50]
    generate_bar_chart(labels, values)
