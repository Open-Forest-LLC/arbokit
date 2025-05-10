from dataclasses import dataclass


@dataclass(frozen=True)
class Colors:
    PRIMARY: str = "#353535"
    BRAND: str = "#009345"
    BACKGROUND_MAIN: str = "#F9FAFB"
    BACKGROUND: str = "#FFFFFF"
    P70: str = "#626262"
    P40: str = "#A5A5A5"
    P20: str = "#D2D2D2"
    P10: str = "#E4E4E4"
    SUCCESS: str = "#009345"
    SUCCESS_HOVER: str = "#4DB47D"
    SUCCESS_PRESSED: str = "#006730"
    ERROR: str = "#FF5959"
    ERROR_HOVER: str = "#FF8B8B"
    ERROR_PRESSED: str = "#B33E3E"
    WARNING: str = "#D07E00"
    WARNING_HOVER: str = "#DFA54D"
    WARNING_PRESSED: str = "#925800"
