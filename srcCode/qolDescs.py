# ------------------QoL texts------------------#

text = {
    "LOADING": "Loading...",
    "DD_STATE": "",
    "DD_OD": ""
}

opts = {
    "DD_STATE": ["Alabama", "Alaska", "Arizona", "Arkansas", 
        "California", "Colorado", "Connecticut", "Delaware", "District of Columbia",
        "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", 
        "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", 
        "Maine", "Maryland", "Massachusetts", "Michigan", 
        "Minnesota", "Mississippi", "Missouri", "Montana", 
        "Nebraska", "Nevada", "New Hampshire", "New Jersey", 
        "New Mexico", "New York", "North Carolina", "North Dakota", 
        "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", 
        "South Carolina", "South Dakota", "Tennessee", "Texas", 
        "Utah", "Vermont", "Virginia", "Washington", "West Virginia", 
        "Wisconsin", "Wyoming"],
    "DD_OD": ["All Drugs", "Any Opioids",
              "Natural, Semi-synthetic, and Synthetic Opioids",
              "Prescription Opioids", "Natural and Semi-synthetic Opioids",
              "Synthetic Opioids besides Methadone", "Methadone", "Heroin"]
}

states = {
    'Alabama': {
        'state_cd': '01',
        'state_abbr': 'AL'
    },
    'Alaska': {
        'state_cd': '02',
        'state_abbr': 'AK'
    },
    'Arizona': {
        'state_cd': '04',
        'state_abbr': 'AZ'
    },
    'Arkansas': {
        'state_cd': '05',
        'state_abbr': 'AR'
    },
    'California': {
        'state_cd': '06',
        'state_abbr': 'CA'
    },
    'Colorado': {
        'state_cd': '08',
        'state_abbr': 'CO'
    },
    'Connecticut': {
        'state_cd': '09',
        'state_abbr': 'CT'
    },
    'Delaware': {
        'state_cd': '10',
        'state_abbr': 'DE'
    },
    'District of Columbia': {
        'state_cd': '11',
        'state_abbr': 'DC'
    },
    'Florida': {
        'state_cd': '12',
        'state_abbr': 'FL'
    },
    'Georgia': {
        'state_cd': '13',
        'state_abbr': 'GA'
    },
    'Hawaii': {
        'state_cd': '15',
        'state_abbr': 'HI'
    },
    'Idaho': {
        'state_cd': '16',
        'state_abbr': 'ID'
    },
    'Illinois': {
        'state_cd': '17',
        'state_abbr': 'IL'
    },
    'Indiana': {
        'state_cd': '18',
        'state_abbr': 'IN'
    },
    'Iowa': {
        'state_cd': '19',
        'state_abbr': 'IA'
    },
    'Kansas': {
        'state_cd': '20',
        'state_abbr': 'KS'
    },
    'Kentucky': {
        'state_cd': '21',
        'state_abbr': 'KY'
    },
    'Louisiana': {
        'state_cd': '22',
        'state_abbr': 'LA'
    },
    'Maine': {
        'state_cd': '23',
        'state_abbr': 'ME'
    },
    'Maryland': {
        'state_cd': '24',
        'state_abbr': 'MD'
    },
    'Massachusetts': {
        'state_cd': '25',
        'state_abbr': 'MA'
    },
    'Michigan': {
        'state_cd': '26',
        'state_abbr': 'MI'
    },
    'Minnesota': {
        'state_cd': '27',
        'state_abbr': 'MN'
    },
    'Mississippi': {
        'state_cd': '28',
        'state_abbr': 'MS'
    },
    'Missouri': {
        'state_cd': '29',
        'state_abbr': 'MO'
    },
    'Montana': {
        'state_cd': '30',
        'state_abbr': 'MT'
    },
    'Nebraska': {
        'state_cd': '31',
        'state_abbr': 'NE'
    },
    'Nevada': {
        'state_cd': '32',
        'state_abbr': 'NV'
    },
    'New Hampshire': {
        'state_cd': '33',
        'state_abbr': 'NH'
    },
    'New Jersey': {
        'state_cd': '34',
        'state_abbr': 'NJ'
    },
    'New Mexico': {
        'state_cd': '35',
        'state_abbr': 'NM'
    },
    'New York': {
        'state_cd': '36',
        'state_abbr': 'NY'
    },
    'North Carolina': {
        'state_cd': '37',
        'state_abbr': 'NC'
    },
    'North Dakota': {
        'state_cd': '38',
        'state_abbr': 'ND'
    },
    'Ohio': {
        'state_cd': '39',
        'state_abbr': 'OH'
    },
    'Oklahoma': {
        'state_cd': '40',
        'state_abbr': 'OK'
    },
    'Oregon': {
        'state_cd': '41',
        'state_abbr': 'OR'
    },
    'Pennsylvania': {
        'state_cd': '42',
        'state_abbr': 'PA'
    },
    'Rhode Island': {
        'state_cd': '44',
        'state_abbr': 'RI'
    },
    'South Carolina': {
        'state_cd': '45',
        'state_abbr': 'SC'
    },
    'South Dakota': {
        'state_cd': '46',
        'state_abbr': 'SD'
    },
    'Tennessee': {
        'state_cd': '47',
        'state_abbr': 'TN'
    },
    'Texas': {
        'state_cd': '48',
        'state_abbr': 'TX'
    },
    'Utah': {
        'state_cd': '49',
        'state_abbr': 'UT'
    },
    'Vermont': {
        'state_cd': '50',
        'state_abbr': 'VT'
    },
    'Virginia': {
        'state_cd': '51',
        'state_abbr': 'VA'
    },
    'Washington': {
        'state_cd': '53',
        'state_abbr': 'WA'
    },
    'West Virginia': {
        'state_cd': '54',
        'state_abbr': 'WV'
    },
    'Wisconsin': {
        'state_cd': '55',
        'state_abbr': 'WI'
    },
    'Wyoming': {
        'state_cd': '56',
        'state_abbr': 'WY'
    },
    'American Samoa': {
        'state_cd': '60',
        'state_abbr': 'AS'
    },
    'Federated States of Micronesia': {
        'state_cd': '64',
        'state_abbr': 'FM     '
    },
    'Guam     ': {
        'state_cd': '66',
        'state_abbr': 'GU'
    },
    'Marshall Islands': {
        'state_cd': '68',
        'state_abbr': 'MH'
    },
    'Commonwealth of the Northern Mariana Islands': {
        'state_cd': '69',
        'state_abbr': 'MP'
    },
    'Palau': {
        'state_cd': '70',
        'state_abbr': 'PW'
    },
    'Puerto Rico': {
        'state_cd': '72',
        'state_abbr': 'PR'
    },
    'U.S. Minor Outlying Islands': {
        'state_cd': '74',
        'state_abbr': 'UM'
    },
    'U.S. Virgin Islands': {
        'state_cd': '78',
        'state_abbr': 'VI'
    }
}

default = {
    "DD_STATE": opts['DD_STATE'][46],
    "DD_OD": opts['DD_OD'][1]
}

ttips = {
    
}