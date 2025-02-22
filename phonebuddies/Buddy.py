class Buddy:
    def __init__(self, row_info):
        self._raw_row_info = row_info

        self._parse_row_attribute("email", 0)
        self._parse_row_attribute("buddy_type", 7)
        self._parse_row_attribute("pseudonym", 1)
        self._parse_row_attribute("full_name", 6, required=False)
        self._parse_row_attribute("phone", 2, required=False)
        self._parse_row_attribute("location", 3, required=False)
        self._parse_row_attribute("time_zone", 4, required=False)
        self._parse_row_attribute("user_message", 5, required=False)

    def __str__(self):
        return "%s (full name: %s): %s" % (self.pseudonym, self.full_name, self.email)

    def _parse_row_attribute(self, attribute_name, row_index, required=True, default="None provided"):
        value = None
        if len(self._raw_row_info) >= row_index + 1:
            new_value = self._raw_row_info[row_index]

            # If a cell is blank but has cells to the right of it that are not blank, the value will be ""
            if new_value != "":
                value = new_value

        if value is None:
            if required:
                raise Exception("ERROR: missing %s data for buddy: %s" % (attribute_name, self._raw_row_info))
            else:
                value = default

        setattr(self, attribute_name, value)

    def contact_text(self):
        return f"""Pseudonym: {self.pseudonym}
Buddy type: {self.buddy_type}
Email: {self.email}
Phone: {self.phone}
Location: {self.location}
Time zone: {self.time_zone}
Introduction: {self.user_message}"""