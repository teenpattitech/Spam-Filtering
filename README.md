[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/warrenferns/Spam-Filtering">
  </a>

  <h3 align="center">Spam-Filtering</h3>

  <p align="center">
    To classify the email into Spam and Non-Spam
    <br />
    <a href="https://github.com/warrenferns/Spam-Filtering"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/warrenferns/Spam-Filtering">View Demo</a>
    ·
    <a href="https://github.com/warrenferns/Spam-Filtering/issues">Report Bug</a>
    ·
    <a href="https://github.com/warrenferns/Spam-Filtering/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Screen Shot][product-screenshot]](https://github.com/warrenferns/Spam-Filtering)

With the help of text-classifier algorithms, rejecting mails based on text analysis can be serious problem in case of false positives. Normally users and organizations would not want any genuine e-mails to be lost. Black list approach has been one of the earliest approaches tried for the filtering of spams. 

The strategy is to accept all the mails except the ones from the domain/e-mail ids. With newer domains entering the category of spamming domains this strategy tends to not work so well. White list approach is the strategy of accepting the mails from the domains/addresses explicitly white listed and put others in a less priority queue, which is delivered only after sender responds to a confirmation request sent by the spam filtering system.

A list of commonly used resources that I find helpful are listed in the acknowledgements.

### Built With

* [Streamlit](https://streamlit.io/)
* [Scikit-learn](https://scikit-learn.org/stable/)
* [NLTK](https://www.nltk.org/)



<!-- GETTING STARTED -->
## Getting Started

### Prerequisites

You need to have Python installed on your PC. If you do not have you can [install from here](https://www.python.org/downloads/)

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/warrenferns/Spam-Filtering
   ```
3. Install the Requirements
   ```sh
   pip install -r requirements.txt
   ```
4. Run the Streamlit App
   ```sh
   streamlit run main.py
   ```



<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Warren Fernandes - [@warrenspeaks](https://twitter.com/warrenspeaks) - warren.fernandes27@gmail.com

Project Link: [https://github.com/warrenferns/Spam-Filtering](https://github.com/warrenferns/Spam-Filtering)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* [Img Shields](https://shields.io)
* [Jupyter Notebook](https://jupyter.org/)
* [GitHub Pages](https://pages.github.com)
* [Animate.css](https://daneden.github.io/animate.css)
* [Loaders.css](https://connoratherton.com/loaders)
* [Slick Carousel](https://kenwheeler.github.io/slick)
* [Smooth Scroll](https://github.com/cferdinandi/smooth-scroll)
* [Sticky Kit](http://leafo.net/sticky-kit)
* [JVectorMap](http://jvectormap.com)
* [Font Awesome](https://fontawesome.com)


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors-anon/warrenferns/Spam-Filtering?color=green&style=for-the-badge
[contributors-url]: https://github.com/warrenferns/Spam-Filtering/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/warrenferns/Spam-Filtering?style=for-the-badge
[forks-url]: https://github.com/warrenferns/Spam-Filtering/network/members
[stars-shield]: https://img.shields.io/github/stars/warrenferns/Spam-Filtering?style=for-the-badge
[stars-url]: https://github.com/warrenferns/Spam-Filtering/stargazers
[issues-shield]: https://img.shields.io/github/issues/warrenferns/Spam-Filtering?color=yellow&style=for-the-badge
[issues-url]: https://github.com/warrenferns/Spam-Filtering/issues
[license-shield]: https://img.shields.io/github/license/othneildrew/Best-README-Template.svg?style=for-the-badge
[license-url]: https://github.com/warrenferns/Spam-Filtering/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/warren-fernandes-a354281a3/
[product-screenshot]: images/screenshot.jpg

