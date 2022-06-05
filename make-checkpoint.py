{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "05e2ce22",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'dict'>\n",
      "      name number Gender  computer_id\n",
      "id                                   \n",
      "1     Juma    128      0            1\n",
      "2     Amos   7080      0            2\n",
      "3    Chris   1234      0            5\n",
      "4   Agatha     76      1            3\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='Gender', ylabel='number of students'>"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "with open(r\"C:\\Users\\GRACE\\Desktop\\lab_system\\db.json\", \"r\") as read_file:\n",
    "    ssp_data = json.load(read_file)\n",
    "\n",
    "print(type(ssp_data))\n",
    "\n",
    "df = pd.DataFrame().from_dict(ssp_data[\"users\"]).set_index(\"id\")\n",
    "print(df)\n",
    "\n",
    "df[\"Gender\"].value_counts().plot(kind=\"bar\", xlabel=\"Gender\", ylabel=\"number of students\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b05865a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
