import math


def triangle(ab: int, bc: int) -> int:
    """
    Для чтения кода - желательно открыть чертеж с условиями задачи.

    BM - медиана, это отрезок который выходит из угла B и делит противолежащую сторону пополам.
    Медиана в прямоугольном треугольнике равна половине гипотенузы AC

    :param ab: int, длина стороны AB
    :param bc: int, длина стороны BC
    :return: int, угол MBC в градусах°
    """

    ac = math.sqrt(ab**2 + bc**2)  # квадрат гипотенузы = сумме квадратов катетов
    bm = mc = ac / 2
    mbc_angle = math.acos((bm**2 + bc**2 - mc**2) / (2 * bm * bc))  # формула вычисления угла по трем сторонам

    # convert rad to degree
    mbc_angle = math.degrees(mbc_angle)

    return round(mbc_angle)


if __name__ == '__main__':
    # side_ab = 20
    # side_bc = 10
    side_ab = int(input())
    side_bc = int(input())
    print(str(triangle(side_ab, side_bc)) + chr(176))  # chr(176) -> '°'
