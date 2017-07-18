"""
Module for calculating Amps
"""

import math

class Amps:

    """Amps"""

    @staticmethod
    def calc_amps_from_voltage_divide_resistance(voltage: float, resistance: float) -> float:

        """calc_amps_from_voltage_divide_resistance
        Will calculate amps from given vulatage and resistance
        :param voltage:
        :type voltage: float
        :param resistance:
        :type resistance: float

        :rtype: float / in ampers
        """
        return voltage / resistance

    @staticmethod
    def calc_amps_from_power_devide_voltage(power: float, voltage: float) -> float:

        """calc_amps_from_power_devide_voltage
        Will calculate amps from giiven power and voltage
        :param power:
        :type power: float
        :param voltage:
        :type voltage: float

        :rtype: float / in ampers
        """
        return power / voltage

    @staticmethod
    def calc_amps_from_sqrt_power_resistance(power: float, resistance: float) -> float:

        """calc_amps_from_sqrt_power_resistance
        Will calculate amps from given power and resitance
        :param power:
        :type power: float
        :param resistance:
        :type resistance: float

        :rtype: float / in ampers
        """
        return math.sqrt(power / resistance)

def calc_amps(**kwargs) -> float:

    """calc_amps - This functions providing a various ways for calculating of amps.

    Allowed kwargs keys are: voltage, resistance and power, kwargs is dict with two keys.
    pair from the previus counted

    This function have a mixed role as dispatcher and factory.

    Based on kwargs will invoke the proper method of calculation. The supported method
    and pair keys are:

    1. When we knowing the voltage and the resistance, the next formula is used: I = U / R

    Important to know is that, all methods will return calculated resistane in AMPS.

    - Example usage:

        >>> from ohmtools import calc_amps
        >>> vr = {'voltage': 12, 'resistance': 100}
        >>> # volatage are in volts and resistance are in ohms
        >>> calc_amps(**vr)
        0.12

    2. When we knowing the power and the voltage, the next formula is used: I = P / V

    - Example usage:

        >>> pv = {'power': 100, 'voltage': 12}
        >>> # power is always in WATTS and voltage is always in VOLTS
        >>> calc_amps(**pv)
        8.33333

    3. When we knowing the power and the resistance, the next formula is used: sqrt(P / R)

    - Example usage:

        >>> pr = {'power': 20, 'resistance': 100}
        >>> calc_amps(**pr)
        0.44721

    :param **kwargs
    :type: kwargs: dict

    rtype: float / in ampers
    """

    assert len(kwargs.keys()) == 2, 'You have to provide two keys'

    if kwargs.get('voltage') and kwargs.get('resistance'):

        return Amps.calc_amps_from_voltage_divide_resistance(
            kwargs.get('voltage'), kwargs.get('resistance')
        )

    if kwargs.get('power') and kwargs.get('voltage'):

        return Amps.calc_amps_from_power_devide_voltage(
            kwargs.get('power'), kwargs.get('voltage')
        )

    if kwargs.get('power') and kwargs.get('resistance'):

        return Amps.calc_amps_from_sqrt_power_resistance(
            kwargs.get('power'), kwargs.get('resistance')
        )

    raise AttributeError('Incorrect configuration')

