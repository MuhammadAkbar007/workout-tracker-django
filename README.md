# Workout Tracker 💪

## Models
### users
 - Django provides **AbstractUser**
    - username, email, password `(hashed by default)`
 - related to workouts `oneToMany`

### exercises
 - name **unique**
 - description
 - or category **null=True blank=True**
    - cardio
    - strength
    - flexibility
    - etc
 - muscle_group **null=True blank=True**
    - chest
    - back
    - legs
    - etc

### workouts
 - user `manyToOne`
 - scheduled_at
 - comment
 - status
    - active
    - pending
    - completed

### workout_exercise `manyToMany`
 - repetition
 - set
 - weight
 - workout **FK**
 - exercise **FK**

## Constraints
> [!NOTE]
> Only authenticated users should be able to create, update, and delete workout plans.
> Needless to say, users should only be able to access their own workout plans.

### System
 - [x] data seeder to populate the database with a list of exercises

## Functions list
### User
 - [x] sign up
 - [x] log in
 - [x] log out
 - [x] refresh tokens

### Workout
 - [x] workout CRUD
    - [x]  **Create Workout:** Allow users to create workouts composed of multiple exercises.
    - [x] **List Workouts:** List active or pending workouts sorted by date and time.
    - [x] **Update Workout:** Allow users to update workouts and add comments.
    - [x] **Delete Workout:** Allow users to delete workouts.
    - [x] **Schedule Workouts:** Allow users to schedule workouts for specific dates and times.
    - [x] **Generate Reports:** Generate reports on past workouts and progress.
 - [x] **only admin can write** exercise CRUD 

