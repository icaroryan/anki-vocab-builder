from flask import Flask, request, render_template, flash, redirect, url_for

app = Flask(__name__)

from app import views
