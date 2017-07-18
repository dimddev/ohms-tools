"""
Module that providing calculations of Ohms
"""

class Ohms:

    """Ohms"""

    @staticmethod
    def calc_ohms_from_voltage_divide_current(voltage: float, current: float) -> float:

        """calc_ohms_from_voltage_divide_current

        :param voltage:
        :type voltage: float
        :param current:
        :type current: float

        :rtype: float
        """
        return voltage / current

    @staticmethod
    def calc_ohms_from_voltate_divide_power(voltage: float, power: float) -> float:

        """calc_ohms_from_voltate_divide_power

        :param voltage:
        :type voltage: float
        :param power:
        :type power: float

        :rtype: float
        """
        return pow(voltage, 2) / power

    @staticmethod
    def calc_ohms_from_power_divide_current(power: float, current: float) -> float:

        """calc_ohms_from_power_divide_current

        :param power:
        :type power: float
        :param current:
        :type current: float

        :rtype: float
        """
        return power / pow(current, 2)


def calc_ohms(**kwargs) -> float:

    """calc_ohms - this function providing various ways for calculating of ohms.

    Allowed kwargs keys are: voltage, current and power, kwargs is dict with two keys.
    pair from the previus counted.

    This function have a mixed role as dispatcher and factory.

    Based on kwargs will invoke the proper method of calculation. The supported method
    and pair keys are:

    1. When we knowing the voltage and the current the next formula is used: R = U / I

    Important to know is that, all methods will return calculated resistane in OHMS.

    - Example usage:

        >>> from ohmtools import calc_ohms
        >>> vr = {'voltage': 12, 'current': 2}
        >>> calc_ohms(**vr)
        6.0
        >>> # is the same as
        >>> calc_ohms(voltage=12, current=2)
        6.0

    2. When we knowing the voltage and the power the next formula is used: pow(voltage, 2) / power

    - Example usage:

        >>> vp = {'voltage': 12, 'power': 100}
        >>> calc_ohms(**vp)
        1.44

    3. When we knowing the power and the current the next formula is used: power / pow(current, 2)

    - Example usage:

        >>> pc = {'power': 100, 'current': 8.333}
        >>> calc_ohms(**pc)
        1.440115206912368

    All other combination or keys will raise to exception beware to catch it if happens

    :param **kwargs
    :type kwargs: dict

    :rtype: float

    """

    assert len(kwargs.keys()) == 2, "You have to provide pair of keys"

    if kwargs.get('voltage') and kwargs.get('current'):

        return Ohms.calc_ohms_from_voltage_divide_current(
            kwargs.get('voltage'), kwargs.get('current')
        )

    if kwargs.get('voltage') and kwargs.get('power'):

        return Ohms.calc_ohms_from_voltate_divide_power(
            kwargs.get('voltage'), kwargs.get('power')
        )

    if kwargs.get('power') and kwargs.get('current'):

        return Ohms.calc_ohms_from_power_divide_current(
            kwargs.get('power'), kwargs.get('current')
        )

    raise AttributeError('Incorrect configuration')

