{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Specify path to read file\n",
    "budget_csv = os.path.join(\"Resources\", \"budget_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    " # New list to store data as int\n",
    "amount = []\n",
    "dates = []"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open file to store values in new list\n",
    "with open(budget_csv, encoding='utf-8-sig') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # Skip header\n",
    "    header = next(csvreader)\n",
    "    \n",
    "    # Create loop to convert string to int\n",
    "    for row in csvreader:\n",
    "        \n",
    "        # Add amounts of \"Profit/Losses\" to new list\n",
    "        amount.append(row[1])\n",
    "        \n",
    "        # Add dates to new list\n",
    "        dates.append(row[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create loop to convert list from string to int\n",
    "for i in range(0, len(amount)): \n",
    "    amount[i] = int(amount[i]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Funtion to calculate total number of records and total amount\n",
    "def total_recrods(numbers):\n",
    "    length = len(numbers)\n",
    "    return length\n",
    "\n",
    "def total(numbers):\n",
    "    sums = sum(numbers)\n",
    "    return sums\n",
    "\n",
    "# Function to calculate average of \"Profit/Losses\"\n",
    "def average(numbers):\n",
    "    return sum(numbers) / float(len(numbers))\n",
    "\n",
    "# Function to calculate greatest increase in profits\n",
    "def increase(numbers):\n",
    "    high = max(numbers)\n",
    "    return high\n",
    "\n",
    "# Function to calculate decrease in losses\n",
    "def decrease(numbers):\n",
    "    low = min(numbers)\n",
    "    return low"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open file to run functions in file data\n",
    "with open(budget_csv, encoding='utf-8-sig') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # Skip header\n",
    "    next(csvreader, None)\n",
    "    \n",
    "   \n",
    "    # Loop through the data to find highest and lowest values\n",
    "    for row in csvreader:\n",
    "\n",
    "        # If the highest increase in a row is equal to 'increase()' function\n",
    "        if(row[1]) == str(increase(amount)):\n",
    "            \n",
    "            # store amount of the highest increase\n",
    "            max_num = (row[1])\n",
    "            \n",
    "            # store date of the highest increase\n",
    "            max_date = (row[0])\n",
    "            \n",
    "        # If the lowest decrease in a row is equal to 'decrease()' function\n",
    "        if(row[1]) == str(decrease(amount)):\n",
    "            \n",
    "            # store amount of the lowest decrease\n",
    "            min_num = (row[1])\n",
    "            \n",
    "            # store date of the lowest decrease\n",
    "            min_date = (row[0])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "# create variables for each statement\n",
    "\n",
    "#The total number of months and amount included in the dataset\n",
    "total_months = total_recrods(amount)\n",
    "total_amount = ' $' + str(total(amount))\n",
    "\n",
    "# The average of the changes in \"Profit/Losses\" over the entire period\n",
    "avg_amount = ' $' + str(round(average(amount), 2))\n",
    "\n",
    "# The greatest increase in profits (date and amount) over the entire period\n",
    "inc_profits = max_date + ' ($' + max_num + ')'\n",
    "\n",
    "# The greatest decrease in losses (date and amount) over the entire period\n",
    "dec_profits = min_date + ' ($' + min_num + ')'"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create a dictionary to store the values\n",
    "dict = {'Total Months: ': total_months, 'Total: ': total_amount, 'Average Change: ': avg_amount,\n",
    "       'Greatest Increase in Profits: ' : inc_profits, 'Greatest Decrease in Profits: ' : dec_profits}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Financial Analysis\n",
      "----------------------------\n",
      "Total Months:  86\n",
      "Total:   $38382578\n",
      "Average Change:   $446309.05\n",
      "Greatest Increase in Profits:  Feb-2012 ($1170593)\n",
      "Greatest Decrease in Profits:  Sep-2013 ($-1196225)\n"
     ]
    }
   ],
   "source": [
    "# Print Financial Analysis\n",
    "print('Financial Analysis')\n",
    "\n",
    "# Print ----------------------------\n",
    "print('----------------------------')\n",
    "\n",
    "# loop to print items in anlaysis\n",
    "for key in dict:\n",
    "    print(key, dict[key])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Example\n",
    "\n",
    "# Financial Analysis\n",
    "# ----------------------------\n",
    "# Total Months: 86\n",
    "# Total: $38382578\n",
    "# Average  Change: $-2315.12\n",
    "# Greatest Increase in Profits: Feb-2012 ($1926159)\n",
    "# Greatest Decrease in Profits: Sep-2013 ($-2196167)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "# In addition, your final script should both print the analysis to the terminal and export a text file with the results."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Specify the file to write to\n",
    "output_path = os.path.join(\"Output\", \"new.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Open the file using \"write\" mode. Specify the variable to hold the contents\n",
    "with open(output_path, 'w') as csvfile:\n",
    "\n",
    "    # Initialize csv.writer\n",
    "    csvwriter = csv.writer(csvfile, delimiter=',')\n",
    "\n",
    "    #Write header row\n",
    "    csvwriter.writerow([\"Financial Analysis\"])\n",
    "\n",
    "    csvwriter.writerows(dict.items())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.7.6"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
