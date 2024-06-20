# SmartAss OnBoard
# Using LexFridman Podcase Transcript specifically
def parse_lex_transcript(soup):
    transcript_segments = soup.find_all('div', class_='ts-segment')
    transcript = ""
    curr_speaker = ""
    curr_response = ""

    for segment in transcript_segments:
        speaker = segment.find('span', class_='ts-name').get_text(strip=True)
        timestamp = segment.find('span', class_='ts-timestamp').get_text(strip=True)
        text = segment.find('span', class_='ts-text').get_text(strip=True)

        if curr_speaker == "":
            curr_speaker = speaker
            curr_response = text 
        elif curr_speaker != speaker:
            transcript += f"\n\n{curr_speaker}: {curr_response}"
            curr_speaker = speaker
            curr_response = text
        elif curr_speaker == speaker:
            curr_response = curr_response.strip() + f" {text}"  

    # Save the trnascript into txt files 
    with open("genius/gen1.txt", "w") as file:
        file.write(transcript.strip())