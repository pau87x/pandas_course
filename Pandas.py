{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c242ae29",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d1d153f6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('words.csv', index_col='Word')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "89bce963",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>be</th>\n",
       "      <td>2</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>and</th>\n",
       "      <td>3</td>\n",
       "      <td>15.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>of</th>\n",
       "      <td>2</td>\n",
       "      <td>18.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum\n",
       "Word              \n",
       "the        3  33.0\n",
       "be         2   5.0\n",
       "and        3  15.0\n",
       "of         2  18.0\n",
       "a          1   1.0"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "1bdefbde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<bound method DataFrame.info of             Length   Sum\n",
       "Word                    \n",
       "the              3  33.0\n",
       "be               2   5.0\n",
       "and              3  15.0\n",
       "of               2  18.0\n",
       "a                1   1.0\n",
       "...            ...   ...\n",
       "early            5  42.0\n",
       "position         8  96.0\n",
       "player           6  57.0\n",
       "agree            5  45.0\n",
       "especially      10   NaN\n",
       "\n",
       "[489 rows x 2 columns]>"
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.info"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "8b4d2147",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(489, 2)"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "4c9d05f0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Length     10.0\n",
       "Sum       114.0\n",
       "Name: community, dtype: float64"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['community']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "fc3caf98",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>489.000000</td>\n",
       "      <td>488.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.865031</td>\n",
       "      <td>50.602459</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.847180</td>\n",
       "      <td>25.410182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>33.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>45.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>62.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13.000000</td>\n",
       "      <td>183.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Length         Sum\n",
       "count  489.000000  488.000000\n",
       "mean     4.865031   50.602459\n",
       "std      1.847180   25.410182\n",
       "min      1.000000    1.000000\n",
       "25%      4.000000   33.000000\n",
       "50%      4.000000   45.000000\n",
       "75%      6.000000   62.000000\n",
       "max     13.000000  183.000000"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "f882e2a5",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "13"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Length'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "17d1f479",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Length     13.0\n",
       "Sum       183.0\n",
       "dtype: float64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "564bc984",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "183.0"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sum'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a42afcde",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "114.0"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc['community','Sum']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "bfc4fa5d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>book</th>\n",
       "      <td>4</td>\n",
       "      <td>36.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>though</th>\n",
       "      <td>6</td>\n",
       "      <td>49.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Length   Sum\n",
       "Word                \n",
       "the          3  33.0\n",
       "book         4  36.0\n",
       "though       6  49.0"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[[\n",
    "    \"the\",\n",
    "    \"book\",\n",
    "    \"though\"\n",
    "]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "b1d93f0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Word\n",
       "the       33.0\n",
       "book      36.0\n",
       "though    49.0\n",
       "Name: Sum, dtype: float64"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[[\n",
    "    \"the\",\n",
    "    \"book\",\n",
    "    \"though\"\n",
    "], 'Sum']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "a21a52fa",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>489.000000</td>\n",
       "      <td>488.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.865031</td>\n",
       "      <td>50.602459</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.847180</td>\n",
       "      <td>25.410182</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>33.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>45.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>62.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13.000000</td>\n",
       "      <td>183.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Length         Sum\n",
       "count  489.000000  488.000000\n",
       "mean     4.865031   50.602459\n",
       "std      1.847180   25.410182\n",
       "min      1.000000    1.000000\n",
       "25%      4.000000   33.000000\n",
       "50%      4.000000   45.000000\n",
       "75%      6.000000   62.000000\n",
       "max     13.000000  183.000000"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "c6bcabd7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>international</th>\n",
       "      <td>13</td>\n",
       "      <td>183.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>development</th>\n",
       "      <td>12</td>\n",
       "      <td>146.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>understand</th>\n",
       "      <td>11</td>\n",
       "      <td>138.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>government</th>\n",
       "      <td>11</td>\n",
       "      <td>137.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>relationship</th>\n",
       "      <td>12</td>\n",
       "      <td>136.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>I</th>\n",
       "      <td>1</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>in</th>\n",
       "      <td>2</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>be</th>\n",
       "      <td>2</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>especially</th>\n",
       "      <td>10</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>489 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "               Length    Sum\n",
       "Word                        \n",
       "international      13  183.0\n",
       "development        12  146.0\n",
       "understand         11  138.0\n",
       "government         11  137.0\n",
       "relationship       12  136.0\n",
       "...               ...    ...\n",
       "I                   1    9.0\n",
       "in                  2    9.0\n",
       "be                  2    5.0\n",
       "a                   1    1.0\n",
       "especially         10    NaN\n",
       "\n",
       "[489 rows x 2 columns]"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values(by=['Sum'], ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "cc0f19eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>international</th>\n",
       "      <td>13</td>\n",
       "      <td>183.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Length    Sum\n",
       "Word                        \n",
       "international      13  183.0"
      ]
     },
     "execution_count": 16,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 183]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "c2804198",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Word\n",
       "the           False\n",
       "be            False\n",
       "and           False\n",
       "of            False\n",
       "a             False\n",
       "              ...  \n",
       "early         False\n",
       "position      False\n",
       "player        False\n",
       "agree         False\n",
       "especially    False\n",
       "Name: Sum, Length: 489, dtype: bool"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df[\"Sum\"] == 183"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "f94e6e78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>them</th>\n",
       "      <td>4</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>remain</th>\n",
       "      <td>6</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>light</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>thank</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "        Length   Sum\n",
       "Word                \n",
       "them         4  50.0\n",
       "remain       6  50.0\n",
       "light        5  50.0\n",
       "thank        5  50.0"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 50]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "06844e9c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0    33.0\n",
       "Name: Sum, dtype: float64"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sum'].mode()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "8c940ee2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>for</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>she</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>him</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>call</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>need</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>high</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>let</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>each</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hold</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kind</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>long</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>long</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pay</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stop</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>buy</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>raise</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>field</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>free</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hope</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Length   Sum\n",
       "Word               \n",
       "the         3  33.0\n",
       "for         3  33.0\n",
       "she         3  33.0\n",
       "all         3  33.0\n",
       "him         3  33.0\n",
       "call        4  33.0\n",
       "need        4  33.0\n",
       "high        4  33.0\n",
       "let         3  33.0\n",
       "each        4  33.0\n",
       "off         3  33.0\n",
       "hold        4  33.0\n",
       "all         3  33.0\n",
       "kind        4  33.0\n",
       "long        4  33.0\n",
       "long        4  33.0\n",
       "pay         3  33.0\n",
       "stop        4  33.0\n",
       "off         3  33.0\n",
       "buy         3  33.0\n",
       "raise       5  33.0\n",
       "field       5  33.0\n",
       "free        4  33.0\n",
       "hope        4  33.0"
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d62c1407",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Sum\n",
       "33.0    24\n",
       "52.0    19\n",
       "45.0    13\n",
       "47.0    12\n",
       "34.0    12\n",
       "Name: count, dtype: int64"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Sum'].value_counts().head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "50e807e4",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>for</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>she</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>him</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>call</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>need</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>high</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>let</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>each</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum\n",
       "Word              \n",
       "the        3  33.0\n",
       "for        3  33.0\n",
       "she        3  33.0\n",
       "all        3  33.0\n",
       "him        3  33.0\n",
       "call       4  33.0\n",
       "need       4  33.0\n",
       "high       4  33.0\n",
       "let        3  33.0\n",
       "each       4  33.0"
      ]
     },
     "execution_count": 22,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33].head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "id": "53fc07f7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum\n",
       "Word              \n",
       "all        3  33.0"
      ]
     },
     "execution_count": 23,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33].sample()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "id": "ccb6ed5f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>she</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>let</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>for</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>long</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hope</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>buy</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>field</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Length   Sum\n",
       "Word               \n",
       "all         3  33.0\n",
       "she         3  33.0\n",
       "off         3  33.0\n",
       "the         3  33.0\n",
       "let         3  33.0\n",
       "for         3  33.0\n",
       "long        4  33.0\n",
       "hope        4  33.0\n",
       "buy         3  33.0\n",
       "field       5  33.0"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33].sample(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "ce0fef78",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>for</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>she</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>him</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>buy</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>let</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pay</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>stop</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>long</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>long</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hold</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>free</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>each</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>high</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>need</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>call</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>kind</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>hope</th>\n",
       "      <td>4</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>raise</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>field</th>\n",
       "      <td>5</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "       Length   Sum\n",
       "Word               \n",
       "the         3  33.0\n",
       "for         3  33.0\n",
       "she         3  33.0\n",
       "all         3  33.0\n",
       "him         3  33.0\n",
       "buy         3  33.0\n",
       "off         3  33.0\n",
       "let         3  33.0\n",
       "pay         3  33.0\n",
       "off         3  33.0\n",
       "all         3  33.0\n",
       "stop        4  33.0\n",
       "long        4  33.0\n",
       "long        4  33.0\n",
       "hold        4  33.0\n",
       "free        4  33.0\n",
       "each        4  33.0\n",
       "high        4  33.0\n",
       "need        4  33.0\n",
       "call        4  33.0\n",
       "kind        4  33.0\n",
       "hope        4  33.0\n",
       "raise       5  33.0\n",
       "field       5  33.0"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33].sort_values(by='Length')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "id": "df38a0b8",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Sum'] == 33, 'Length'].min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "id": "6da4ad99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>for</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>she</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>him</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>let</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>all</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>pay</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>off</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>buy</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum\n",
       "Word              \n",
       "the        3  33.0\n",
       "for        3  33.0\n",
       "she        3  33.0\n",
       "all        3  33.0\n",
       "him        3  33.0\n",
       "let        3  33.0\n",
       "off        3  33.0\n",
       "all        3  33.0\n",
       "pay        3  33.0\n",
       "off        3  33.0\n",
       "buy        3  33.0"
      ]
     },
     "execution_count": 27,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[\n",
    "    (df['Sum'] == 33) &\n",
    "    (df['Length'] == 3)\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "id": "357bf8ff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>pay</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum\n",
       "Word              \n",
       "pay        3  33.0"
      ]
     },
     "execution_count": 28,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[\n",
    "    (df['Sum'] == 33) &\n",
    "    (df['Length'] == 3)\n",
    "].sample(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "1eb235a0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['Ratio'] = df['Sum'] / df['Length']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "id": "3229656c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>count</th>\n",
       "      <td>489.000000</td>\n",
       "      <td>488.000000</td>\n",
       "      <td>488.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>mean</th>\n",
       "      <td>4.865031</td>\n",
       "      <td>50.602459</td>\n",
       "      <td>10.193517</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>std</th>\n",
       "      <td>1.847180</td>\n",
       "      <td>25.410182</td>\n",
       "      <td>2.486249</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>min</th>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>25%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>33.000000</td>\n",
       "      <td>8.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>50%</th>\n",
       "      <td>4.000000</td>\n",
       "      <td>45.000000</td>\n",
       "      <td>10.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>75%</th>\n",
       "      <td>6.000000</td>\n",
       "      <td>62.000000</td>\n",
       "      <td>11.678571</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>max</th>\n",
       "      <td>13.000000</td>\n",
       "      <td>183.000000</td>\n",
       "      <td>22.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "           Length         Sum       Ratio\n",
       "count  489.000000  488.000000  488.000000\n",
       "mean     4.865031   50.602459   10.193517\n",
       "std      1.847180   25.410182    2.486249\n",
       "min      1.000000    1.000000    1.000000\n",
       "25%      4.000000   33.000000    8.500000\n",
       "50%      4.000000   45.000000   10.333333\n",
       "75%      6.000000   62.000000   11.678571\n",
       "max     13.000000  183.000000   22.000000"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "930e0aa6",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Word\n",
       "the       11.000000\n",
       "book       9.000000\n",
       "though     8.166667\n",
       "Name: Ratio, dtype: float64"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[[\n",
    "    \"the\",\n",
    "    \"book\",\n",
    "    \"though\"\n",
    "], 'Ratio']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "id": "1ee8a0cb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>the</th>\n",
       "      <td>3</td>\n",
       "      <td>33.0</td>\n",
       "      <td>11.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>be</th>\n",
       "      <td>2</td>\n",
       "      <td>5.0</td>\n",
       "      <td>2.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>and</th>\n",
       "      <td>3</td>\n",
       "      <td>15.0</td>\n",
       "      <td>5.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>of</th>\n",
       "      <td>2</td>\n",
       "      <td>18.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>a</th>\n",
       "      <td>1</td>\n",
       "      <td>1.0</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum  Ratio\n",
       "Word                     \n",
       "the        3  33.0   11.0\n",
       "be         2   5.0    2.5\n",
       "and        3  15.0    5.0\n",
       "of         2  18.0    9.0\n",
       "a          1   1.0    1.0"
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "c44dee14",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "22.0"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['Ratio'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "id": "252ba211",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>3</td>\n",
       "      <td>66.0</td>\n",
       "      <td>22.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>us</th>\n",
       "      <td>2</td>\n",
       "      <td>39.0</td>\n",
       "      <td>19.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>to</th>\n",
       "      <td>2</td>\n",
       "      <td>39.0</td>\n",
       "      <td>19.500000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>our</th>\n",
       "      <td>3</td>\n",
       "      <td>52.0</td>\n",
       "      <td>17.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>your</th>\n",
       "      <td>4</td>\n",
       "      <td>64.0</td>\n",
       "      <td>16.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum      Ratio\n",
       "Word                         \n",
       "you        3  66.0  22.000000\n",
       "us         2  39.0  19.500000\n",
       "to         2  39.0  19.500000\n",
       "our        3  52.0  17.333333\n",
       "your       4  64.0  16.000000"
      ]
     },
     "execution_count": 34,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.sort_values(by='Ratio', ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f6f65847",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>3</td>\n",
       "      <td>66.0</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum  Ratio\n",
       "Word                     \n",
       "you        3  66.0   22.0"
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Ratio'] == 22]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "25e37b86",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 3)"
      ]
     },
     "execution_count": 36,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Ratio'] == 22].shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "2438b4ef",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1, 3)"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Ratio == 22\").shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "163a01da",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>two</th>\n",
       "      <td>3</td>\n",
       "      <td>30.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>even</th>\n",
       "      <td>4</td>\n",
       "      <td>40.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>another</th>\n",
       "      <td>7</td>\n",
       "      <td>70.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>member</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>six</th>\n",
       "      <td>3</td>\n",
       "      <td>30.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>light</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>return</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>even</th>\n",
       "      <td>4</td>\n",
       "      <td>40.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>thank</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Length   Sum  Ratio\n",
       "Word                        \n",
       "two           3  30.0   10.0\n",
       "even          4  40.0   10.0\n",
       "another       7  70.0   10.0\n",
       "member        6  60.0   10.0\n",
       "six           3  30.0   10.0\n",
       "light         5  50.0   10.0\n",
       "return        6  60.0   10.0\n",
       "even          4  40.0   10.0\n",
       "thank         5  50.0   10.0"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Ratio == 10\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "f0247f42",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>another</th>\n",
       "      <td>7</td>\n",
       "      <td>70.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>member</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>return</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>light</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>thank</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>even</th>\n",
       "      <td>4</td>\n",
       "      <td>40.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>even</th>\n",
       "      <td>4</td>\n",
       "      <td>40.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>two</th>\n",
       "      <td>3</td>\n",
       "      <td>30.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>six</th>\n",
       "      <td>3</td>\n",
       "      <td>30.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Length   Sum  Ratio\n",
       "Word                        \n",
       "another       7  70.0   10.0\n",
       "member        6  60.0   10.0\n",
       "return        6  60.0   10.0\n",
       "light         5  50.0   10.0\n",
       "thank         5  50.0   10.0\n",
       "even          4  40.0   10.0\n",
       "even          4  40.0   10.0\n",
       "two           3  30.0   10.0\n",
       "six           3  30.0   10.0"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Ratio == 10\").sort_values(by='Sum', ascending=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "a7c3bf39",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>another</th>\n",
       "      <td>7</td>\n",
       "      <td>70.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>member</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>return</th>\n",
       "      <td>6</td>\n",
       "      <td>60.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>light</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>thank</th>\n",
       "      <td>5</td>\n",
       "      <td>50.0</td>\n",
       "      <td>10.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         Length   Sum  Ratio\n",
       "Word                        \n",
       "another       7  70.0   10.0\n",
       "member        6  60.0   10.0\n",
       "return        6  60.0   10.0\n",
       "light         5  50.0   10.0\n",
       "thank         5  50.0   10.0"
      ]
     },
     "execution_count": 41,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Ratio == 10\").sort_values(by='Sum', ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "1cc17b2b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "66.0"
      ]
     },
     "execution_count": 42,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Ratio'] == 22, 'Sum'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "id": "ec551b9b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>3</td>\n",
       "      <td>66.0</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum  Ratio\n",
       "Word                     \n",
       "you        3  66.0   22.0"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[\n",
    "    (df['Ratio'] == 22) &\n",
    "    (df['Sum'] == 66)\n",
    "]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "9ee3c895",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 44,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Ratio'] == 22, 'Length'].max()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "586b2952",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "3"
      ]
     },
     "execution_count": 46,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.loc[df['Ratio'] == 22, 'Length'].min()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "8c9f5fbd",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>you</th>\n",
       "      <td>3</td>\n",
       "      <td>66.0</td>\n",
       "      <td>22.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Length   Sum  Ratio\n",
       "Word                     \n",
       "you        3  66.0   22.0"
      ]
     },
     "execution_count": 47,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query('Ratio == 22').sort_values(by=\"Length\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "ef3b9eff",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "4.865030674846626"
      ]
     },
     "execution_count": 49,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "mean_char_count = df['Length'].mean()\n",
    "mean_char_count"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "449f85b2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>their</th>\n",
       "      <td>5</td>\n",
       "      <td>74.0</td>\n",
       "      <td>14.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>would</th>\n",
       "      <td>5</td>\n",
       "      <td>72.0</td>\n",
       "      <td>14.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>about</th>\n",
       "      <td>5</td>\n",
       "      <td>49.0</td>\n",
       "      <td>9.8</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>there</th>\n",
       "      <td>5</td>\n",
       "      <td>52.0</td>\n",
       "      <td>10.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>think</th>\n",
       "      <td>5</td>\n",
       "      <td>57.0</td>\n",
       "      <td>11.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>early</th>\n",
       "      <td>5</td>\n",
       "      <td>42.0</td>\n",
       "      <td>8.4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>position</th>\n",
       "      <td>8</td>\n",
       "      <td>96.0</td>\n",
       "      <td>12.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>player</th>\n",
       "      <td>6</td>\n",
       "      <td>57.0</td>\n",
       "      <td>9.5</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>agree</th>\n",
       "      <td>5</td>\n",
       "      <td>45.0</td>\n",
       "      <td>9.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>especially</th>\n",
       "      <td>10</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>242 rows × 3 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "            Length   Sum  Ratio\n",
       "Word                           \n",
       "their            5  74.0   14.8\n",
       "would            5  72.0   14.4\n",
       "about            5  49.0    9.8\n",
       "there            5  52.0   10.4\n",
       "think            5  57.0   11.4\n",
       "...            ...   ...    ...\n",
       "early            5  42.0    8.4\n",
       "position         8  96.0   12.0\n",
       "player           6  57.0    9.5\n",
       "agree            5  45.0    9.0\n",
       "especially      10   NaN    NaN\n",
       "\n",
       "[242 rows x 3 columns]"
      ]
     },
     "execution_count": 50,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Length > @mean_char_count\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "id": "4f365ba3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Length</th>\n",
       "      <th>Sum</th>\n",
       "      <th>Ratio</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Word</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>international</th>\n",
       "      <td>13</td>\n",
       "      <td>183.0</td>\n",
       "      <td>14.076923</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>development</th>\n",
       "      <td>12</td>\n",
       "      <td>146.0</td>\n",
       "      <td>12.166667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>relationship</th>\n",
       "      <td>12</td>\n",
       "      <td>136.0</td>\n",
       "      <td>11.333333</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>government</th>\n",
       "      <td>11</td>\n",
       "      <td>137.0</td>\n",
       "      <td>12.454545</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>understand</th>\n",
       "      <td>11</td>\n",
       "      <td>138.0</td>\n",
       "      <td>12.545455</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "               Length    Sum      Ratio\n",
       "Word                                   \n",
       "international      13  183.0  14.076923\n",
       "development        12  146.0  12.166667\n",
       "relationship       12  136.0  11.333333\n",
       "government         11  137.0  12.454545\n",
       "understand         11  138.0  12.545455"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.query(\"Length > @mean_char_count\").sort_values(by='Length', ascending=False).head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f9970786",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2de3aba3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e4bd87a6",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bdf5e530",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1960bd40",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4c92e106",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "38054d73",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d01ea3fa",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "edcc24c2",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a53a0fdd",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "406b5703",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b87c3e5d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "05c184b5",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a2b4ea8",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
