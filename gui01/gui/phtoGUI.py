# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Dec 17 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MainForm
###########################################################################

class MainForm ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Photo Matcher", pos = wx.DefaultPosition, size = wx.Size( 992,500 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHints( wx.Size( 850,500 ), wx.DefaultSize )

        bSizer4 = wx.BoxSizer( wx.VERTICAL )

        bSizer14 = wx.BoxSizer( wx.HORIZONTAL )

        sbSizer2 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Inputs" ), wx.VERTICAL )

        sbSizer2.SetMinSize( wx.Size( -1,100 ) )
        bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText1 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"\nImage Root Folder :    ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )

        bSizer5.Add( self.m_staticText1, 0, 0, 5 )

        self.m_dirPicker1 = wx.DirPickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.m_dirPicker1.SetMinSize( wx.Size( 500,-1 ) )

        bSizer5.Add( self.m_dirPicker1, 0, wx.ALL, 5 )


        sbSizer2.Add( bSizer5, 1, wx.EXPAND, 5 )

        bSizer6 = wx.BoxSizer( wx.HORIZONTAL )

        self.m_staticText11 = wx.StaticText( sbSizer2.GetStaticBox(), wx.ID_ANY, u"\nImage Dest Folder :  ", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText11.Wrap( -1 )

        bSizer6.Add( self.m_staticText11, 0, wx.ALL, 5 )

        self.m_dirPicker4 = wx.DirPickerCtrl( sbSizer2.GetStaticBox(), wx.ID_ANY, wx.EmptyString, u"Select a folder", wx.DefaultPosition, wx.DefaultSize, wx.DIRP_DEFAULT_STYLE )
        self.m_dirPicker4.SetMinSize( wx.Size( 500,-1 ) )

        bSizer6.Add( self.m_dirPicker4, 0, wx.ALL, 5 )


        sbSizer2.Add( bSizer6, 1, wx.EXPAND, 5 )


        bSizer14.Add( sbSizer2, 1, wx.EXPAND, 5 )

        sbSizer3 = wx.StaticBoxSizer( wx.StaticBox( self, wx.ID_ANY, u"Options" ), wx.VERTICAL )

        self.cbReplace = wx.CheckBox( sbSizer3.GetStaticBox(), wx.ID_ANY, u"Replace If exists", wx.DefaultPosition, wx.DefaultSize, 0 )
        sbSizer3.Add( self.cbReplace, 0, wx.ALL, 5 )


        bSizer14.Add( sbSizer3, 1, wx.EXPAND, 5 )


        bSizer4.Add( bSizer14, 1, wx.EXPAND, 5 )

        bSizer13 = wx.BoxSizer( wx.HORIZONTAL )

        self.butCancel = wx.Button( self, wx.ID_ANY, u"Cancel", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.butCancel, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.butCopy = wx.Button( self, wx.ID_ANY, u"Start", wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer13.Add( self.butCopy, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

        self.m_gauge1 = wx.Gauge( self, wx.ID_ANY, 100, wx.DefaultPosition, wx.DefaultSize, wx.GA_HORIZONTAL )
        self.m_gauge1.SetValue( 0 )
        bSizer13.Add( self.m_gauge1, 0, wx.ALL, 5 )


        bSizer4.Add( bSizer13, 1, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        bSizer8 = wx.BoxSizer( wx.VERTICAL )

        self.m_scrolledWindow2 = wx.ScrolledWindow( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.HSCROLL|wx.VSCROLL )
        self.m_scrolledWindow2.SetScrollRate( 5, 5 )
        self.m_scrolledWindow2.SetMinSize( wx.Size( -1,500 ) )

        bSizer8.Add( self.m_scrolledWindow2, 1, wx.EXPAND |wx.ALL, 5 )


        bSizer4.Add( bSizer8, 1, wx.EXPAND, 5 )


        self.SetSizer( bSizer4 )
        self.Layout()

        self.Centre( wx.BOTH )

    def __del__( self ):
        pass


