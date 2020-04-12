# Actions

Actions enable complex sequences of actions to be callable from a simple interface.

## Psuedo code example

```python
psuedo code
add servos

add new action called walk
walk = Action('walk')
walk.add_step('set servo:left_leg angle=90')
walk.add_step('pause=0.1')
walk.add_step('set servo:left_foot angle=30')
actions.add(walk)

    add step set servo(leftleg).to_angle = 90
    add step set servo(leftfoot).to_angle = 30
    add step set pause 0.1
    add step set servo[rightleg].to_angle = 0
    add step set servo(rightfoot).to_angle = 30
```
