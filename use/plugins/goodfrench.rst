
.. _plugin-goodfrench:

The GoodFrench plugin
=====================

Command
-------

.. _command-goodfrench-detect:

goodfrench detect <texte>
^^^^^^^^^^^^^^^^^^^^^^^^^

Cherche des fautes dans le *<texte>*, en fonction de la valeur locale de
:ref:`supybot.plugins.GoodFrench.level.`



.. _plugin-goodfrench-config:

Configuration
-------------

.. _supybot.plugins.GoodFrench.level:

supybot.plugins.GoodFrench.level
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: 0

Le niveau de filtrage. Le niveau N filtre ce que le niveau N-1 filtrait, avec des choses en plus. 0 : pas de filtrage ; 1 : filtre le langage SMS 2 : filtre les erreurs de pluriel ; 3 : filtre les fautes de conjugaison courantes ; 4 : filtre les fautes d'orthographe courantes ; 5 : filtre les abbréviations ("t'as" au lieu de "tu as") ; 6 : filtre les 'lol' 7 : filtre les erreurs de typographie (note : a tendance à avoir la gachette facile)

.. _supybot.plugins.GoodFrench.public:

supybot.plugins.GoodFrench.public
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Default value: True

Determines whether this plugin is publicly visible.

