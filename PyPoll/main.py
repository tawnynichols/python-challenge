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
    "voter_csv = os.path.join(\"Resources\", \"election_data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "# New dictionary and lists to store candidate names, votes, and percent\n",
    "myDict = {} \n",
    "candidate_names = []\n",
    "candidate_votes = []\n",
    "candidate_percent = []\n",
    "total_votes = 0"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "# open file to store values in new list\n",
    "with open(voter_csv, encoding='utf-8-sig') as csvfile:\n",
    "    csvreader = csv.reader(csvfile, delimiter=\",\")\n",
    "    \n",
    "    # Skip header\n",
    "    header = next(csvreader)\n",
    "    \n",
    "    # Create loop to convert string to int\n",
    "    for row in csvreader:\n",
    "        row[0] = int(row[0])\n",
    "        \n",
    "        #Count total records with votes\n",
    "        total_votes = total_votes + 1\n",
    "        \n",
    "        # Add unqie canidate names to new list\n",
    "        if row[2] not in candidate_names:\n",
    "            candidate_names.append(row[2])\n",
    "            \n",
    "            # Add place holders to votes list\n",
    "            candidate_votes.append(0)\n",
    "        \n",
    "        # loop to count votes per candidate\n",
    "        for j in candidate_names:    \n",
    "            if row[2] == j:\n",
    "                candidate_votes[candidate_names.index(j)] += 1       "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop to add votes to candidate votes list\n",
    "for v in candidate_votes:\n",
    "    candidate_percent.append(round((v / total_votes)*100, 4))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop to find the winner of the election based on popular vote.\n",
    "for x in candidate_votes:\n",
    "    if x == max(candidate_votes):\n",
    "        winner_index = (candidate_votes.index(x))\n",
    "        winner = candidate_names[winner_index]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Loop to add the elements in list to create dictionary for each candidate\n",
    "for val in candidate_names: \n",
    "    myDict.setdefault(val, []).append(candidate_percent[candidate_names.index(val)]) \n",
    "    myDict.setdefault(val, []).append(candidate_votes[candidate_names.index(val)]) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Create function to print anlaysis\n",
    "def title_print():\n",
    "    print(\"Election Results\")\n",
    "    print(\"-------------------------\")\n",
    "\n",
    "# Print total votes\n",
    "def total_votes_print():\n",
    "    print(f'Total Votes: {total_votes}')\n",
    "    print(\"-------------------------\")\n",
    "\n",
    "# Print the list of candidates, percentage of votes, and candidates' total votes\n",
    "def analysis_print():\n",
    "    \n",
    "    for key, value in myDict.items():\n",
    "        print (f'{key}: {value[0]}00% ({value[1]})')     \n",
    "        \n",
    "# Print winner\n",
    "def winner_print():\n",
    "    print(\"-------------------------\")\n",
    "    print(f'Winner: {winner}')\n",
    "    print(\"-------------------------\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "# Export a text file with the results\n",
    "\n",
    "# Specify the file to write to\n",
    "output_path = os.path.join(\"analysis\", \"election_output.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Election Results\n",
      "-------------------------\n",
      "Total Votes: 3521001\n",
      "-------------------------\n",
      "Khan: 63.000% (2218231)\n",
      "Correy: 20.000% (704200)\n",
      "Li: 14.000% (492940)\n",
      "O'Tooley: 3.000% (105630)\n",
      "-------------------------\n",
      "Winner: Khan\n",
      "-------------------------\n"
     ]
    }
   ],
   "source": [
    "# Open the file using \"write\" mode. Specify the variable to hold the contents\n",
    "with open(output_path, 'w') as csvfile:\n",
    "\n",
    "    # Initialize csv.writer\n",
    "    csvwriter = csv.writer(csvfile, delimiter=',')\n",
    "\n",
    "    #Write header row\n",
    "    csvwriter.writerow([\"Election Results\"])\n",
    "    csvwriter.writerow([\"Total Votes:\", total_votes])\n",
    "    for key, value in myDict.items():\n",
    "        csvwriter.writerows([[key, str(value[0])+\"00%\", value[1]]])\n",
    "    csvwriter.writerow([\"Winner:\", winner])\n",
    "\n",
    "# Print the analysis to the terminal\n",
    "title_print()\n",
    "total_votes_print()\n",
    "analysis_print()\n",
    "winner_print()"
   ]
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
