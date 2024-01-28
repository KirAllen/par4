import math


def pearson_correlation(array_1, array_2):
    """
    ������ ���������� ������� ����� ����� ���������.

    Args:
     - array_1: ������ ������ ��������
     - array_2: ������ ������ ��������

    Return:
     - ���������� ������� ����� ��������� array_1 � array_2
    """

    # �������� �� ��, ��� ������� ���������� �����
    if len(array_1) != len(array_2):
        raise ValueError("������� ������ ���� ���������� �����")

    n = len(array_1)

    # ������ �������� ��������
    mean_x = sum(array_1) / n
    mean_y = sum(array_2) / n

    variance_x = sum([(xi - mean_x) ** 2 for xi in array_1]) / float(len(array_1))
    variance_y = sum([(yi - mean_y) ** 2 for yi in array_2]) / float(len(array_2))

    covariance = sum([(xi - mean_x) * (yi - mean_y) for xi, yi in zip(array_1, array_2)]) / float(len(array_1))
    correlation = covariance / (math.sqrt(variance_x * variance_y))

    return correlation


array_1 = [3, 5, 8, 15, 20, 25, 31, 35, 42]
array_2 = [2, 3, 4, 7, 12, 17, 23, 28, 33]

correlation = round(pearson_correlation(array_1, array_2), 4)
print(f"���������� �������: {correlation}")