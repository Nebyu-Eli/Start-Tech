# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:11:58 2022

@author: hp
"""

import sqlite3


class Database8:
    def __init__(self, db8):
        self.conn = sqlite3.connect(db8)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS matches (id INTEGER PRIMARY KEY,IDD text ,city text, date text, player_of_match text,venue text, neutral_venue text, team1 text, team2 text, toss_winner text, toss_decision text, winner text, result text, result_margin text, eliminator text, method text, umpire1 text, umpire2 text )")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM matches")
        rows = self.cur.fetchall()
        return rows

    def insert(self, IDD,city, date, player_of_match,venue, neutral_venue, team1, team2, toss_winner, toss_decision , winner, result, result_margin, eliminator, method, umpire1, umpire2):
        self.cur.execute("INSERT INTO matches VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (IDD, city, date, player_of_match,venue, neutral_venue, team1, team2, toss_winner, toss_decision, winner, result, result_margin, eliminator, method, umpire1, umpire2))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM matches WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id,IDD, city, date, player_of_match,venue, neutral_venue, team1, team2, toss_winner, toss_decision , winner, result, result_margin, eliminator, method, umpire1, umpire2):
        self.cur.execute("UPDATE matches SET IDD = ?, city = ?, date = ?, player_of_match = ?,venue = ?, neutral_venue = ?, team1 = ?, team2 = ?, toss_winner = ?, toss_decision = ?, winner = ?, result = ?, result_margin = ?, eliminator = ?, method = ?, umpire1 = ?, umpire2 = ? WHERE id = ?",
                         (IDD,city, date, player_of_match,venue, neutral_venue, team1, team2, toss_winner, toss_decision , winner, result, result_margin, eliminator, method, umpire1, umpire2, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()