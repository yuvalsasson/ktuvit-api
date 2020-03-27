Unofficial python client to ktuvit.me API

Usage is pretty straight forward:
```python
import ktuvit

api = ktuvit.KtuvitApi()

api.find_series("Subtitle", "Prodigal.Son.S01E07.720p.HDTV.x264-KILLERS", 1,1) # Possible search_types are FilmName, Subtitle, ImdbID (case sensetive)
api.find_film('ImdbID', 'tt5463162') # Deadpool 2
"""
Should return something like this:
{
    'ErrorMessage': None,
    'IsSuccess': True,
    'Results': [{'Identifier': 'B01A861744343E9201D4ED1C73378559','SubtitleName': 'Deadpool.2.2018.NEW.720p.HD-TC.X264-CPG'}
}
"""

subtitle = api.get_subtitle('B01A861744343E9201D4ED1C73378559') # get the specified subtitles
# Save the subtitles to a file
with open("out.srt", "wb") as out:
    out.write(subtitle)
```
see documentation for more information.