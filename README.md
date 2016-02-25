# Posts

<http://kylebebak.github.io/posts/>

Code, __TILs__, inspired by [jbranchaud/til](https://github.com/jbranchaud/til), and rants about other stuff, like music and footy. The site itself is generated by __Jekyll__ and hosted by GitHub, using the wonderful and free __GitHub Pages__. The markdown for the site map is generated by Python scripts in [_map](_map).

## Continuous Integration
Done via Git hooks. These live in [_hooks](_hooks), and are deployed to `.git/hooks`, like this:

~~~sh
cd .git/hooks && ln -s -f ../../_hooks/* ./
~~~

After commits, `site-map.md` and `_includes/sidebar.md` are regenerated. Before pushing to `master`, the subdirectory `_site` is automatically pushed to `gh-pages`, which regenerates <http://kylebebak.github.io/posts/>.

To check links, I run [LinkChecker](https://github.com/wummel/linkchecker/) against the site, using:

~~~sh
# local
linkchecker --no-warnings http://127.0.0.1:4000/posts/
# production
linkchecker --no-warnings http://kylebebak.github.io/posts/
~~~

I don't use `LinkChecker` in Git hooks because it takes a while to run. The relevant field in the output is `Parent URL`, which points to the file containing a broken link.

## License

Everything in this repo is licensed under the [MIT License](https://opensource.org/licenses/MIT).
