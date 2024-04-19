from website_analyzer import crawl_website
from test_case_generator import load_wcag_guidelines, identify_applicable_personas, generate_bdd_test_cases
from test_runner import execute_tests

def main():
    url = "https://www.educative.io/courses/grokking-the-low-level-design-interview-using-ood-principles"  # Replace with the target website URL
    soup, wcag_info = crawl_website(url)
    wcag_guidelines = load_wcag_guidelines()
    applicable_personas = identify_applicable_personas(soup, wcag_info, wcag_guidelines)
    test_cases = generate_bdd_test_cases(applicable_personas)
    execute_tests(test_cases, url)

if __name__ == "__main__":
    main()