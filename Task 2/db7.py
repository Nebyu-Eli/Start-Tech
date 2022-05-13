# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:01:02 2022

@author: hp
"""
import sqlite3


class Database7:
    def __init__(self, db7):
        self.conn = sqlite3.connect(db7)
        self.cur = self.conn.cursor()
        self.cur.execute(
            "CREATE TABLE IF NOT EXISTS IPL_ball (id INTEGER PRIMARY KEY, IDD text,winning text, over text, ball text,batsman text, non_striker text, bowler text, batsman_runs text, extra_runs text, total_runs text, is_wicket text, dismissal_kind text, player_dismissed text, fielder text, extras_type text, batting_team text, bowling_team text )")
        self.conn.commit()

    def fetch(self):
        self.cur.execute("SELECT * FROM IPL_ball")
        rows = self.cur.fetchall()
        return rows

    def insert(self, IDD,winning, over, ball,batsman, non_striker, bowler, batsman_runs, extra_runs, total_runs, is_wicket, dismissal_kind, player_dismissed, fielder, extras_type, batting_team, bowling_team):
        self.cur.execute("INSERT INTO IPL_ball VALUES (NULL, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                         (IDD,winning, over, ball,batsman, non_striker, bowler, batsman_runs, extra_runs, total_runs, is_wicket, dismissal_kind, player_dismissed, fielder, extras_type, batting_team, bowling_team))
        self.conn.commit()

    def remove(self, id):
        self.cur.execute("DELETE FROM IPL_ball WHERE id=?", (id,))
        self.conn.commit()

    def update(self, id, IDD,winning, over, ball,batsman, non_striker, bowler, batsman_runs, extra_runs, total_runs, is_wicket, dismissal_kind, player_dismissed, fielder, extras_type, batting_team, bowling_team):
        self.cur.execute("UPDATE IPL_ball SET IDD = ?, winning = ?, over = ?, ball = ?,batsman = ?, non_striker = ?, bowler = ?, batsman_runs = ?, extra_runs = ?, total_runs = ?, is_wicket = ?, dismissal_kind = ?, player_dismissed = ?, fielder = ?, extras_type = ?, batting_team = ?, bowling_team = ? WHERE id = ?",
                         (IDD, winning, over, ball,batsman, non_striker, bowler, batsman_runs, extra_runs, total_runs, is_wicket, dismissal_kind, player_dismissed, fielder, extras_type, batting_team, bowling_team, id))
        self.conn.commit()

    def __del__(self):
        self.conn.close()