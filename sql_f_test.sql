CREATE TABLE "Film"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "type" VARCHAR(255) NOT NULL,
    "description" VARCHAR(255) NOT NULL,
    "director" VARCHAR(255) NOT NULL,
    "image_url" bytea NOT NULL
);
ALTER TABLE
    "Film" ADD PRIMARY KEY("id");
CREATE TABLE "Music"(
    "id" SERIAL NOT NULL,
    "name" VARCHAR(255) NOT NULL,
    "author" VARCHAR(255) NOT NULL,
    "url" bytea NOT NULL
);
ALTER TABLE
    "Music" ADD PRIMARY KEY("id");
CREATE TABLE "Film_Music"(
    "id" SERIAL NOT NULL,
    "film_id" INTEGER NOT NULL,
    "music_id" INTEGER NOT NULL
);
ALTER TABLE
    "Film_Music" ADD PRIMARY KEY("id");
CREATE TABLE "User"(
    "telegram_id" INTEGER NOT NULL,
    "fullname" VARCHAR(255) NOT NULL
);
ALTER TABLE
    "User" ADD PRIMARY KEY("telegram_id");
CREATE TABLE "LikedMusic"(
    "id" SERIAL NOT NULL,
    "user_id" INTEGER NOT NULL,
    "music_id" INTEGER NOT NULL
);
ALTER TABLE
    "LikedMusic" ADD PRIMARY KEY("id");
CREATE TABLE "MusicActivity"(
    "music_id" INTEGER NOT NULL,
    "count_get" INTEGER NOT NULL
);
ALTER TABLE
    "MusicActivity" ADD PRIMARY KEY("music_id");
CREATE TABLE "FilmActivity"(
    "film_id" INTEGER NOT NULL,
    "count_get" INTEGER NOT NULL
);
ALTER TABLE
    "FilmActivity" ADD PRIMARY KEY("film_id");
CREATE TABLE "UserSettings"(
    "user_id" INTEGER NOT NULL,
    "language" VARCHAR(255) NOT NULL,
    "list_count" SMALLINT NOT NULL
);
ALTER TABLE
    "UserSettings" ADD PRIMARY KEY("user_id");
CREATE TABLE "TopUsers"(
    "user_id" INTEGER NOT NULL,
    "rating" DOUBLE PRECISION NOT NULL
);
ALTER TABLE
    "TopUsers" ADD PRIMARY KEY("user_id");
ALTER TABLE
    "LikedMusic" ADD CONSTRAINT "likedmusic_music_id_foreign" FOREIGN KEY("music_id") REFERENCES "Music"("id") ON DELETE CASCADE;
ALTER TABLE
    "Film_Music" ADD CONSTRAINT "film_music_music_id_foreign" FOREIGN KEY("music_id") REFERENCES "Music"("id") ON DELETE CASCADE;
ALTER TABLE
    "LikedMusic" ADD CONSTRAINT "likedmusic_user_id_foreign" FOREIGN KEY("user_id") REFERENCES "User"("telegram_id") ON DELETE CASCADE;
ALTER TABLE
    "Film_Music" ADD CONSTRAINT "film_music_film_id_foreign" FOREIGN KEY("film_id") REFERENCES "Film"("id") ON DELETE CASCADE;