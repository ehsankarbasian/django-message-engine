from abc import ABC


class FormItemInterface(ABC):
    pass


class Input(FormItemInterface):
    pass


class SubmitButton(FormItemInterface):
    pass


class RadioButton(FormItemInterface):
    pass


class FormItems:
    Input = Input
    SubmitButton = SubmitButton
    RadioButton = RadioButton
