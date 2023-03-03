import matplotlib.pyplot as plt


def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels=labels)
    ax.axis('equal')
    plt.show()


if __name__ == '__name__':
    labels = ['a', 'b', 'c']
    values = [10, 100, 150]
    generate_pie_chart(labels, values)
