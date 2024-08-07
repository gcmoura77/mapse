/*

=========================================================
* AppSeed - Simple SCSS compiler via Gulp
=========================================================

*/

var autoprefixer = require('gulp-autoprefixer');
var browserSync = require('browser-sync').create();
var cleanCss = require('gulp-clean-css');
var gulp = require('gulp');
const npmDist = require('gulp-npm-dist');
var sass = require('gulp-sass')(require('node-sass'));
var wait = require('gulp-wait');
var sourcemaps = require('gulp-sourcemaps');
var rename = require("gulp-rename");
const uglify = require('gulp-uglify');

// Define COMMON paths

const paths = {
    src: {
        base: './',
        css: './css',
        scss: './scss',
        node_modules: './node_modules/',
        vendor: './vendor',
        js: './js'
    }
};

// Compile SCSS
gulp.task('scss', function() {
    return gulp.src([paths.src.scss + '/material-dashboard.scss'])
        .pipe(wait(500))
        .pipe(sourcemaps.init())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer({
            overrideBrowserslist: ['> 1%']
        }))
        .pipe(sourcemaps.write('.'))
        .pipe(gulp.dest(paths.src.css))
        .pipe(browserSync.stream());
});

// CSS
gulp.task('css', function() {
    return gulp.src([
            paths.src.css + '/material-dashboard.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Minify CSS
gulp.task('minify:css', function() {
    return gulp.src([
            paths.src.css + '/material-dashboard.css'
        ])
        .pipe(cleanCss())
        .pipe(rename(function(path) {
            // Updates the object in-place
            path.extname = ".min.css";
        }))
        .pipe(gulp.dest(paths.src.css))
});

// Minify JS
gulp.task('minify-js', function() {
    return gulp.src([paths.src.js + '/material-dashboard.js'])  
        .pipe(sourcemaps.init())
        .pipe(uglify())
        .pipe(rename({ suffix: '.min' }))
        .pipe(sourcemaps.write('.'))  // Escreve o .map no mesmo diretório que o arquivo .min.js
        .pipe(gulp.dest(paths.src.js));  
});

// Default Task: Compile SCSS and minify the result
gulp.task('default', gulp.series('scss', 'minify:css', 'minify-js'));
