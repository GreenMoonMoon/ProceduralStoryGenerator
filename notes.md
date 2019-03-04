# GENERAL NOTES
* The templates system is the basis of this program. A simple but extensive format is require.
* In order to avoid echo chamber where generated content is always the same due to constant focus on player interests, the engine needs to chanlenge or conflict the players interests and choices. However, as with everything, this needs to be balanced.
## Templates
The general idea of templates is to offer an easy to use relation database. A template requires some inputs to be complete and then returns a series of relations between various story elements. A general example would be the protagonist, generaly the player, and its quest. The protagonist seeks to complete its quest and once he or she does, the story ends. If the quest is not completed then the story continues.
This example is extremely simple but illustrate the basis of our template system. The first element is the narrative thread, lets use the term *narreme*, a single thread of ideas of events that unfold linearly. The narreme may have one or more variables that are substitued by the engine for elements that seems the most appropriate, the player as the *hero* and the game objective as the *quest* for example. The second element is the choice or the condition. At one point the next narreme, the story ending, depends on a *completion* condition of the previous narreme. If the quest element isn't completed then the story ending cannot happend.
Narreme themselves should be able to reference one another, in our example, the *quest* narreme may consist of a few other narreme defining each step of this quest and the generator should be able to substitue narreme as it would other elements, selecting the most appropriate for the current storyline.
To summarize, templates need to consist of granular element, the narreme. Each narreme needs to hold variables that may be substitued for other narreme or game elements. Narreme should be able to specify conditionnal elements and appropriate corresponding return value.

JSON is a good starting point, it dictionnary like structure provide a nice base to our own format.
```
{
    "_info": {"version": "0.0.1", "name": "generic_quest"},
    "_origin": "{hero} must complete {quest:complete}{complete?:good_ending|bad_ending}",
    "quest": "the journey to slay {villain}",
    "good_ending": "the hero lived happily ever after",
    "bad_ending": "the hero died trying, dooming us all"
}
```
In that example we see the basis of the format. **`_`** attributes are reserved, such as `_info` and `_origin`. Names enclosed in **`{}`** are variables which may be swaped for other elements or narremes by the enging. Notice that there is no semantic differences between a narreme variable or a game elements one, The engine treats the narreme and the game elements as the same. Howevere conflicts may occure, in that case the correct behavior should be defined wheter is to just trow an exception, lets the game elements override the narreme or the other way around. Then we have the **`:`** which denote a return value and in the case of `{complete?:ending}` if paired with **`?`** creates a condition. The **`|`** acts as an *else*. Variables can be nested, `this {variable?:isTrue|{otherVariable?:optionA|optionB}}`
This syntaxt could be tedious in the long run.