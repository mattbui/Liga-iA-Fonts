## This is the master list of ligatures that ligaturize.py will attempt to copy
## from Fira Code to your output font. Ligatures that aren't present in the
## version of Fira Code you're using will be skipped.
## To disable ligatures, simply comment them out in this file.
ligatures = [
    {
        ## These are all the punctuation characters used in Fira Code ligatures.
        ## Use the `--copy-character-glyphs` option to copy these into the output
        ## font along with the ligatures themselves.
        'chars': [
            ## These characters generally look good in most fonts and are
            ## enabled by default if you use `--copy-character-glyphs`.
            'asciicircum', 'asciitilde', 'asterisk',
            'equal', 'greater', 'hyphen',
            'less', 'numbersign', 'plus',
            'slash',  'backslash', 'underscore',
        ],
        'firacode_ligature_name': None,
    },
    {   # ^=
        'chars': ['asciicircum', 'equal'],
        'firacode_ligature_name': 'asciicircum_equal.liga',
    },
    {   # ~~
        'chars': ['asciitilde', 'asciitilde'],
        'firacode_ligature_name': 'asciitilde_asciitilde.liga',
    },
    {   # ~~>
        'chars': ['asciitilde', 'asciitilde', 'greater'],
        'firacode_ligature_name': 'asciitilde_asciitilde_greater.liga',
    },
    {   # ~=
        'chars': ['asciitilde', 'equal'],
        'firacode_ligature_name': 'asciitilde_equal.liga',
    },
    {   # ~>
        'chars': ['asciitilde', 'greater'],
        'firacode_ligature_name': 'asciitilde_greater.liga',
    },
    {   # ~-
        'chars': ['asciitilde', 'hyphen'],
        'firacode_ligature_name': 'asciitilde_hyphen.liga',
    },
    {   # *>
        'chars': ['asterisk', 'greater'],
        'firacode_ligature_name': 'asterisk_greater.liga',
    },
    {   # */
        'chars': ['asterisk', 'slash'],
        'firacode_ligature_name': 'asterisk_slash.liga',
    },
    {   # ||
        'chars': ['bar', 'bar'],
        'firacode_ligature_name': 'bar_bar.liga',
    },
    {   # |||>
        'chars': ['bar', 'bar', 'bar', 'greater'],
        'firacode_ligature_name': 'bar_bar_bar_greater.liga',
    },
    {   # ||=
        'chars': ['bar', 'bar', 'equal'],
        'firacode_ligature_name': 'bar_bar_equal.liga',
    },
    {   # ||>
        'chars': ['bar', 'bar', 'greater'],
        'firacode_ligature_name': 'bar_bar_greater.liga',
    },
    {   # ||-  # new in 2.0
        'chars': ['bar', 'bar', 'hyphen'],
        'firacode_ligature_name': 'bar_bar_hyphen.liga',
    },
    {   # |}
        'chars': ['bar', 'braceright'],
        'firacode_ligature_name': 'bar_braceright.liga',
    },
    {   # |]
        'chars': ['bar', 'bracketright'],
        'firacode_ligature_name': 'bar_bracketright.liga',
    },
    {   # |=
        'chars': ['bar', 'equal'],
        'firacode_ligature_name': 'bar_equal.liga',
    },
    {   # |=>  # new in 2.0
        'chars': ['bar', 'equal', 'greater'],
        'firacode_ligature_name': 'bar_equal_greater.liga',
    },
    {   # |>
        'chars': ['bar', 'greater'],
        'firacode_ligature_name': 'bar_greater.liga',
    },
    {   # |-
        'chars': ['bar', 'hyphen'],
        'firacode_ligature_name': 'bar_hyphen.liga',
    },
    {   # |->  # new in 2.0
        'chars': ['bar', 'hyphen', 'greater'],
        'firacode_ligature_name': 'bar_hyphen_greater.liga',
    },
    {   # {|
        'chars': ['braceleft', 'bar'],
        'firacode_ligature_name': 'braceleft_bar.liga',
    },
    {   # [|
        'chars': ['bracketleft', 'bar'],
        'firacode_ligature_name': 'bracketleft_bar.liga',
    },
    {   # ==
        'chars': ['equal', 'equal'],
        'firacode_ligature_name': 'equal_equal.liga',
    },
    {   # ===
        'chars': ['equal', 'equal', 'equal'],
        'firacode_ligature_name': 'equal_equal_equal.liga',
    },
    {   # ==>
        'chars': ['equal', 'equal', 'greater'],
        'firacode_ligature_name': 'equal_equal_greater.liga',
    },
    {   # =>
        'chars': ['equal', 'greater'],
        'firacode_ligature_name': 'equal_greater.liga',
    },
    {   # =>>
        'chars': ['equal', 'greater', 'greater'],
        'firacode_ligature_name': 'equal_greater_greater.liga',
    },
    {   # =<<
        'chars': ['equal', 'less', 'less'],
        'firacode_ligature_name': 'equal_less_less.liga',
    },
    {   # =/=
        'chars': ['equal', 'slash', 'equal'],
        'firacode_ligature_name': 'equal_slash_equal.liga',
    },
    {   # !=
        'chars': ['exclam', 'equal'],
        'firacode_ligature_name': 'exclam_equal.liga',
    },
    {   # !==
        'chars': ['exclam', 'equal', 'equal'],
        'firacode_ligature_name': 'exclam_equal_equal.liga',
    },
    {   # >=
        'chars': ['greater', 'equal'],
        'firacode_ligature_name': 'greater_equal.liga',
    },
    {   # >=>
        'chars': ['greater', 'equal', 'greater'],
        'firacode_ligature_name': 'greater_equal_greater.liga',
    },
    {   # >>
        'chars': ['greater', 'greater'],
        'firacode_ligature_name': 'greater_greater.liga',
    },
    {   # >>=
        'chars': ['greater', 'greater', 'equal'],
        'firacode_ligature_name': 'greater_greater_equal.liga',
    },
    {   # >>>
        'chars': ['greater', 'greater', 'greater'],
        'firacode_ligature_name': 'greater_greater_greater.liga',
    },
    {   # >>-
        'chars': ['greater', 'greater', 'hyphen'],
        'firacode_ligature_name': 'greater_greater_hyphen.liga',
    },
    {   # >-
        'chars': ['greater', 'hyphen'],
        'firacode_ligature_name': 'greater_hyphen.liga',
    },
    {   # >->
        'chars': ['greater', 'hyphen', 'greater'],
        'firacode_ligature_name': 'greater_hyphen_greater.liga',
    },
    {   # -~
        'chars': ['hyphen', 'asciitilde'],
        'firacode_ligature_name': 'hyphen_asciitilde.liga',
    },
    {   # -|
        'chars': ['hyphen', 'bar'],
        'firacode_ligature_name': 'hyphen_bar.liga',
    },
    {   # ->
        'chars': ['hyphen', 'greater'],
        'firacode_ligature_name': 'hyphen_greater.liga',
    },
    {   # ->>
        'chars': ['hyphen', 'greater', 'greater'],
        'firacode_ligature_name': 'hyphen_greater_greater.liga',
    },
    {   # --
        'chars': ['hyphen', 'hyphen'],
        'firacode_ligature_name': 'hyphen_hyphen.liga',
    },
    {   # -->
        'chars': ['hyphen', 'hyphen', 'greater'],
        'firacode_ligature_name': 'hyphen_hyphen_greater.liga',
    },
    {   # ---
        'chars': ['hyphen', 'hyphen', 'hyphen'],
        'firacode_ligature_name': 'hyphen_hyphen_hyphen.liga',
    },
    {   # -<
        'chars': ['hyphen', 'less'],
        'firacode_ligature_name': 'hyphen_less.liga',
    },
    {   # -<<
        'chars': ['hyphen', 'less', 'less'],
        'firacode_ligature_name': 'hyphen_less_less.liga',
    },
    {   # <~
        'chars': ['less', 'asciitilde'],
        'firacode_ligature_name': 'less_asciitilde.liga',
    },
    {   # <~~
        'chars': ['less', 'asciitilde', 'asciitilde'],
        'firacode_ligature_name': 'less_asciitilde_asciitilde.liga',
    },
    {   # <~>
        'chars': ['less', 'asciitilde', 'greater'],
        'firacode_ligature_name': 'less_asciitilde_greater.liga',
    },
    {   # <*
        'chars': ['less', 'asterisk'],
        'firacode_ligature_name': 'less_asterisk.liga',
    },
    {   # <*>
        'chars': ['less', 'asterisk', 'greater'],
        'firacode_ligature_name': 'less_asterisk_greater.liga',
    },
    {   # <|
        'chars': ['less', 'bar'],
        'firacode_ligature_name': 'less_bar.liga',
    },
    {   # <||
        'chars': ['less', 'bar', 'bar'],
        'firacode_ligature_name': 'less_bar_bar.liga',
    },
    {   # <|||
        'chars': ['less', 'bar', 'bar', 'bar'],
        'firacode_ligature_name': 'less_bar_bar_bar.liga',
    },
    {   # <|>
        'chars': ['less', 'bar', 'greater'],
        'firacode_ligature_name': 'less_bar_greater.liga',
    },
    {   # <=
        'chars': ['less', 'equal'],
        'firacode_ligature_name': 'less_equal.liga',
    },
    {   # <=|  # new in 2.0
        'chars': ['less', 'equal', 'bar'],
        'firacode_ligature_name': 'less_equal_bar.liga',
    },
    {   # <==
        'chars': ['less', 'equal', 'equal'],
        'firacode_ligature_name': 'less_equal_equal.liga',
    },
    {   # <=>
        'chars': ['less', 'equal', 'greater'],
        'firacode_ligature_name': 'less_equal_greater.liga',
    },
    {   # <=<
        'chars': ['less', 'equal', 'less'],
        'firacode_ligature_name': 'less_equal_less.liga',
    },
    {   # <>
        'chars': ['less', 'greater'],
        'firacode_ligature_name': 'less_greater.liga',
    },
    {   # <-
        'chars': ['less', 'hyphen'],
        'firacode_ligature_name': 'less_hyphen.liga',
    },
    {   # <-|  # new in 2.0
        'chars': ['less', 'hyphen', 'bar'],
        'firacode_ligature_name': 'less_hyphen_bar.liga',
    },
    {   # <->
        'chars': ['less', 'hyphen', 'greater'],
        'firacode_ligature_name': 'less_hyphen_greater.liga',
    },
    {   # <--
        'chars': ['less', 'hyphen', 'hyphen'],
        'firacode_ligature_name': 'less_hyphen_hyphen.liga',
    },
    {   # <-<
        'chars': ['less', 'hyphen', 'less'],
        'firacode_ligature_name': 'less_hyphen_less.liga',
    },
    {   # <<
        'chars': ['less', 'less'],
        'firacode_ligature_name': 'less_less.liga',
    },
    {   # <<=
        'chars': ['less', 'less', 'equal'],
        'firacode_ligature_name': 'less_less_equal.liga',
    },
    {   # <<-
        'chars': ['less', 'less', 'hyphen'],
        'firacode_ligature_name': 'less_less_hyphen.liga',
    },
    {   # <<<
        'chars': ['less', 'less', 'less'],
        'firacode_ligature_name': 'less_less_less.liga',
    },
    {   # <+
        'chars': ['less', 'plus'],
        'firacode_ligature_name': 'less_plus.liga',
    },
    {   # <+>
        'chars': ['less', 'plus', 'greater'],
        'firacode_ligature_name': 'less_plus_greater.liga',
    },
    {   # </
        'chars': ['less', 'slash'],
        'firacode_ligature_name': 'less_slash.liga',
    },
    {   # </>
        'chars': ['less', 'slash', 'greater'],
        'firacode_ligature_name': 'less_slash_greater.liga',
    },
    {   # .=
        'chars': ['period', 'equal'],
        'firacode_ligature_name': 'period_equal.liga',
    },
    {   # .-
        'chars': ['period', 'hyphen'],
        'firacode_ligature_name': 'period_hyphen.liga',
    },
    {   # +>
        'chars': ['plus', 'greater'],
        'firacode_ligature_name': 'plus_greater.liga',
    },
    {   # ++
        'chars': ['plus', 'plus'],
        'firacode_ligature_name': 'plus_plus.liga',
    },
    {   # +++
        'chars': ['plus', 'plus', 'plus'],
        'firacode_ligature_name': 'plus_plus_plus.liga',
    },
    {   # /*
        'chars': ['slash', 'asterisk'],
        'firacode_ligature_name': 'slash_asterisk.liga',
    },
    {   # /=
        'chars': ['slash', 'equal'],
        'firacode_ligature_name': 'slash_equal.liga',
    },
    {   # /==
        'chars': ['slash', 'equal', 'equal'],
        'firacode_ligature_name': 'slash_equal_equal.liga',
    },
    {   # />
        'chars': ['slash', 'greater'],
        'firacode_ligature_name': 'slash_greater.liga',
    },
    {   # _|_
        'chars': ['underscore', 'bar', 'underscore'],
        'firacode_ligature_name': 'underscore_bar_underscore.liga',
    },
    {   # __
        'chars': ['underscore', 'underscore'],
        'firacode_ligature_name': 'underscore_underscore.liga',
    },
    {   # <==>
        'chars': ['less', 'equal','equal','greater'],
        'firacode_ligature_name': 'less_equal_equal_greater.liga',
    },
]
