
module.exports = function(grunt) {

	// Project configuration.
	grunt.initConfig({
		cssmin: {
		  target: {
		    files: {
		      'css/main.min.css': ['css/main.css']
		    }
		  }
		},
		// uglify: {
		//     my_target: {
		//       files: {
		//         'js-min/scripts.min.js': ['js/1.js', 'js/2.js', 'js/c3.min.js']
		//       }
		//     }
		//   },
	  concat: {
	  	 map: {
	  	 	src: ['bower_components/jquery/dist/jquery.min.map'],
	  	 	dest: 'build/js/jquery.min.map',
	  	 },
	    js: {
	      src: ['bower_components/jquery/dist/jquery.min.js',
	      		'bower_components/bootstrap/dist/js/bootstrap.min.js',
	      		'bower_components/d3/d3.min.js',
	      		'js/c3.min.js'],
	      dest: 'build/js/scripts.min.js',
	    },
	    css: {
	      src: ['bower_components/bootstrap/dist/css/bootstrap.min.css',
	      		'css/main.min.css', 
	      		'css/c3.min.css'],
	      dest: 'build/css/styles.min.css',
	    },
	  },
	  watch: {
	    js: {
	      files: ['js/**/*.js'],
	      tasks: ['concat:js'],
	    },
	    css: {
	      files: ['css/**/*.css'],
	      tasks: ['concat:css'],
	    },
	  }, 
	});

	grunt.loadNpmTasks('grunt-contrib-cssmin');
	// grunt.loadNpmTasks('grunt-contrib-uglify');
	grunt.loadNpmTasks('grunt-contrib-concat');
	grunt.loadNpmTasks('grunt-contrib-watch');
	grunt.registerTask('default', ['cssmin', 'concat', 'watch'])

};