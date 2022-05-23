brick_types = {
    0: {
        "title": "none",
    },
    1: {
        "title": "ordinary",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
            "grey",
        ],
    },
    2: {
        "title": "flashing",
        "hits": 1,
        "drop": "+10 points",
        "sprite": "star",
        "color": [
            "grey0",
            "grey10",
            "grey20",
            "grey30",
            "grey40",
            "grey50",
            "grey60",
            "grey70",
            "grey80",
            "grey90",
            "grey100",
            "grey90",
            "grey80",
            "grey70",
            "grey60",
            "grey50",
            "grey40",
            "grey30",
            "grey20",
            "grey10",
            "grey0",
        ],
    },
    3: {
        "title": "multi-hit",
        "hits": 5,
        "drop": "",
        "sprite": "",
        "color": [
            "firebrick1",
            "firebrick2",
            "firebrick3",
            "firebrick",
            "firebrick4",
        ],
    },
    4: {
        "title": "indestructible",
        "hits": -1,
        "drop": "",
        "sprite": "",
        "color": [
            "gray50"
            "gray70",
        ],
    },
    5: {
        "title": "brick_row",
        "hits": 1,
        "drop": "bricks",
        "sprite": "",
        "color": [
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chartreuse3",
            "chartreuse2",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chartreuse3",
            "chartreuse2",
            "chartreuse2",
            "chartreuse3",
            "chartreuse4",
            "chartreuse3",
            "chartreuse2",
        ],
    },
    6: {
        "title": "less_points",
        "hits": 1,
        "drop": "-10 points",
        "sprite": "",
        "color": [
        ],
    },
    7: {
        "title": "more_lives",
        "hits": 1,
        "drop": "+1 life",
        "sprite": "heart",
        "color": [
            "green"
        ],
    },
    8: {
        "title": "less_lives",
        "hits": 1,
        "drop": "-1 life",
        "sprite": "",
        "color": [
        ],
    },
    9: {
        "title": "gun",
        "hits": 1,
        "drop": "gun",
        "sprite": "",
        "color": [
        ],
    },
    10: {
        "title": "steel ball",
        "hits": 1,
        "drop": "punch through bricks",
        "sprite": "",
        "color": [
        ],
    },
    11: {
        "title": "boundary",
        "hits": 1,
        "drop": "bricks below paddle",
        "sprite": "",
        "color": [
        ],
    },
    12: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    13: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    14: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    15: {
        "title": "",
        "hits": 1,
        "drop": "",
        "color": [
        ],
    },
    16: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    17: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    18: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    19: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
    20: {
        "title": "",
        "hits": 1,
        "drop": "",
        "sprite": "",
        "color": [
        ],
    },
}

levels = {
    0: {"background": "gradient_1",
        "layout": [
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [2, 2, 7, 7, 2, 2, 7, 7, 2, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ],
        },
    1: {"background": "gradient_1",
        "layout": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0, 0, 1, 1, 0],
            [0, 1, 2, 1, 0, 0, 1, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        ],
        },
    2: {"background": "gradient_2",
        "layout": [
            [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
            [0, 0, 3, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 1, 1, 0, 0, 2, 1, 1, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
        ],
        },
    3: {"background": "gradient_1",
        "layout": [
            [1, 1, 1, 3, 3, 3, 3, 1, 1, 1],
            [1, 1, 1, 0, 2, 2, 0, 1, 1, 1],
            [1, 1, 2, 2, 0, 0, 2, 2, 1, 1],
            [0, 1, 1, 0, 2, 2, 0, 1, 1, 0],
            [0, 0, 3, 3, 0, 0, 3, 3, 0, 0],
            [0, 0, 0, 3, 0, 0, 3, 0, 0, 0],
        ],
        },
    4: {"background": "gradient_2",
        "layout": [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 1, 3, 0, 0, 3, 1, 1, 0],
            [0, 1, 2, 2, 0, 0, 2, 2, 1, 0],
            [0, 1, 1, 0, 2, 2, 0, 1, 1, 0],
            [0, 0, 3, 3, 0, 0, 3, 3, 0, 0],
            [1, 0, 0, 3, 0, 0, 3, 0, 0, 1],
        ],
        },

}
