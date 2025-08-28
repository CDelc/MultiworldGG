from enum import IntFlag

import comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 as __wrapper_module__
from comtypes.gen._00020430_0000_0000_C000_000000000046_0_2_0 import (
    OLE_COLOR, Font, Library, OLE_YPOS_HIMETRIC, IFontEventsDisp,
    IFont, FONTNAME, OLE_YSIZE_PIXELS, Gray, OLE_YPOS_PIXELS, HRESULT,
    CoClass, OLE_XPOS_HIMETRIC, FONTBOLD, OLE_XPOS_CONTAINER, dispid,
    COMMETHOD, OLE_YSIZE_HIMETRIC, EXCEPINFO, Monochrome,
    OLE_OPTEXCLUSIVE, Unchecked, IFontDisp, Default, Color,
    typelib_path, FONTSTRIKETHROUGH, FontEvents, IEnumVARIANT,
    FONTITALIC, Checked, OLE_CANCELBOOL, IDispatch, FONTUNDERSCORE,
    OLE_XSIZE_CONTAINER, DISPPROPERTY, OLE_XSIZE_HIMETRIC, GUID,
    OLE_YPOS_CONTAINER, StdFont, OLE_YSIZE_CONTAINER, _lcid,
    _check_version, BSTR, VARIANT_BOOL, OLE_XSIZE_PIXELS, DISPPARAMS,
    StdPicture, DISPMETHOD, OLE_ENABLEDEFAULTBOOL, FONTSIZE,
    OLE_XPOS_PIXELS, VgaColor, IUnknown, IPicture, Picture,
    OLE_HANDLE, IPictureDisp
)


class OLE_TRISTATE(IntFlag):
    Unchecked = 0
    Checked = 1
    Gray = 2


class LoadPictureConstants(IntFlag):
    Default = 0
    Monochrome = 1
    VgaColor = 2
    Color = 4


__all__ = [
    'FONTUNDERSCORE', 'OLE_XSIZE_CONTAINER', 'OLE_COLOR', 'Font',
    'Library', 'LoadPictureConstants', 'OLE_YPOS_HIMETRIC',
    'IFontEventsDisp', 'IFont', 'FONTNAME', 'OLE_XSIZE_HIMETRIC',
    'OLE_YSIZE_PIXELS', 'OLE_TRISTATE', 'OLE_YPOS_CONTAINER',
    'StdFont', 'OLE_YSIZE_CONTAINER', 'Gray', 'OLE_CANCELBOOL',
    'OLE_YPOS_PIXELS', 'OLE_XPOS_HIMETRIC', 'FONTBOLD',
    'OLE_XPOS_CONTAINER', 'OLE_XSIZE_PIXELS', 'StdPicture',
    'OLE_YSIZE_HIMETRIC', 'Monochrome', 'OLE_OPTEXCLUSIVE',
    'Unchecked', 'IFontDisp', 'Default', 'Color',
    'OLE_ENABLEDEFAULTBOOL', 'FONTSIZE', 'typelib_path',
    'OLE_XPOS_PIXELS', 'FONTSTRIKETHROUGH', 'FontEvents', 'VgaColor',
    'FONTITALIC', 'Checked', 'IPicture', 'Picture', 'OLE_HANDLE',
    'IPictureDisp'
]

